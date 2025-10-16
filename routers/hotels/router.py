from fastapi import APIRouter
from routers.hotels.dao import HotelDAO
from routers.hotels.schemas import BookingWithRoomResponse
from datetime import date
from fastapi_cache.decorator import cache
from typing import List

router = APIRouter()


@cache(expire=60)
@router.get("/{location}")
async def get_hotels_by_name(
        location: str,
        date_from: date,
        date_to: date
) -> List[BookingWithRoomResponse]:
    return await HotelDAO.find_hotels_with_available_rooms(
        location,
        date_from,
        date_to
    )

