from fastapi import APIRouter, HTTPException, Query, Path
from datetime import date
from routers.hotels.rooms.service import RoomService
from routers.hotels.rooms.dao import RoomDAO

router = APIRouter()


@router.get("/hotel/{hotel_id}")
async def get_available_rooms_in_hotel(
        hotel_id: int = Path(..., description="ID отеля"),
        date_from: date = Query(..., description="Дата заезда"),
        date_to: date = Query(..., description="Дата выезда"),
):
    """
    Получение свободных номеров в конкретном отеле
    """
    try:
        rooms = await RoomService.get_available_rooms(
            hotel_id=hotel_id,
            date_from=date_from,
            date_to=date_to
        )

        if not rooms:
            raise HTTPException(404, "Свободные номера не найдены")

        return rooms

    except ValueError as e:
        raise HTTPException(400, str(e))


@router.get("/{room_id}")
async def get_room_details(
        room_id: int = Path(..., description="ID номера")
):
    """
    Получение детальной информации о номере
    """
    try:
        room = await RoomService.get_room_details(room_id)
        return room
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.get("/hotel/{hotel_id}/all")
async def get_all_rooms_in_hotel(
        hotel_id: int = Path(..., description="ID отеля")
):
    """
    Получение всех номеров отеля (без учета доступности)
    """
    rooms = await RoomDAO.find_all_by_hotel_id(hotel_id)

    if not rooms:
        raise HTTPException(404, "Номера не найдены")

    return rooms