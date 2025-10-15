from fastapi import APIRouter, Depends
from routers.bookings.dao import BookingsDAO
from routers.bookings.schemas import SBooking
from routers.bookings.exceptions import CannotBookedException
from routers.users.depends import get_user_from_sub
from datetime import date
from models.users import Users

router = APIRouter()


@router.post("/create")
async def add_booking(
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_user_from_sub)
    ):
    booking = await BookingsDAO.add(
        room_id=room_id,
        user_id=user.id,
        date_to=date_to,
        date_from=date_from
    )
    if not booking:
        raise CannotBookedException



@router.get("/get")
async def get_all(
        user = Depends(get_user_from_sub)
) -> list[SBooking]:
    """
    Получить все бронирования по авторизованному пользователю
    """
    return await BookingsDAO.select_all(user_id=user.id)


