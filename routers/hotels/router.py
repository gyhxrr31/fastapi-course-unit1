from fastapi import APIRouter
from routers.hotels.dao import HotelDAO
from routers.hotels.schemas import BookingWithRoomResponse
from datetime import date

router = APIRouter()



@router.get("/{hotel_name}")
async def get_hotels_by_name(
        location: str,
        date_from: date,
        date_to: date
) -> BookingWithRoomResponse:
    return await HotelDAO.find_hotels_with_available_rooms(
        location,
        date_from,
        date_to
    )

