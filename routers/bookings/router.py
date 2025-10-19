from fastapi import APIRouter, Depends, Form
from routers.bookings.dao import BookingsDAO
from routers.bookings.schemas import SBooking
from routers.bookings.exceptions import CannotBookedException
from routers.users.depends import get_user_from_sub
from datetime import date
from models.users import Users
from tasks.tasks import send_booking_confirmation_email
from routers.bookings.utils import sqlalchemy_to_dict

router = APIRouter()


@router.post("/create")
async def add_booking(
    room_id: int = Form(...),
    date_from: date = Form(...),
    date_to: date = Form(...),
    user: Users = Depends(get_user_from_sub)
    ):
    booking = await BookingsDAO.add_bookings(
        room_id=room_id,
        user_id=user.id,
        date_to=date_to,
        date_from=date_from
    )
    send_booking_confirmation_email.delay(sqlalchemy_to_dict(booking), user.email)
    if not booking:
        raise CannotBookedException


@router.delete("/delete")
async def delete_booking_by_user(
        user: Users = Depends(get_user_from_sub),
        room_id: int = Form(...)
) -> None:
   return await BookingsDAO.delete_booking(
       user_id=user.id,
       room_id=room_id
   )




@router.get("/get")
async def get_all(
        user = Depends(get_user_from_sub)
) -> list[SBooking]:
    """
    Получить все бронирования по авторизованному пользователю
    """
    return await BookingsDAO.select_all(user_id=user.id)


