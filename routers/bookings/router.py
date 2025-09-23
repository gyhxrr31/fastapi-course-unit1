from fastapi import APIRouter, Depends
from routers.bookings.dao import BookingsDAO
from routers.bookings.schemas import SBooking
from routers.users.depends import get_user_from_sub

router = APIRouter()


@router.post("/create")
def add_booking():
    pass


@router.get("/get")
async def get_all(
        user = Depends(get_user_from_sub)
) -> list[SBooking]:
    """
    Получить все бронирования по авторизованному пользователю
    """
    return await BookingsDAO.select_all(user_id=user.id)


