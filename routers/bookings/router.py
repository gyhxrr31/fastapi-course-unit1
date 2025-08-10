from fastapi import APIRouter
from routers.bookings.dao import BookingsService
from routers.bookings.schemas import SBooking

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.post("/create")
def add_booking():
    pass

@router.get("/get")
async def get_all() -> list[SBooking]:
    """
    Получить все бронирования
    """
    return await BookingsService.select_all()


