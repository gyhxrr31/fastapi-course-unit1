from datetime import date
from routers.hotels.rooms.dao import RoomDAO
from typing import List

class RoomService:
    @staticmethod
    async def get_available_rooms(
            hotel_id: int,
            date_from: date,
            date_to: date
    ) -> List[dict]:
        """
        Получает свободные номера в отеле с дополнительной информацией
        """
        # Валидация дат
        if date_from >= date_to:
            raise ValueError("Дата выезда должна быть после даты заезда")

        if (date_to - date_from).days > 30:
            raise ValueError("Максимальный период бронирования - 30 дней")

        return await RoomDAO.find_available_rooms_by_hotel(
            hotel_id=hotel_id,
            date_from=date_from,
            date_to=date_to
        )

    @staticmethod
    async def get_room_details(room_id: int) -> dict:
        """
        Получает детальную информацию о номере
        """
        room = await RoomDAO.get_room_with_hotel_info(room_id)
        if not room:
            raise ValueError("Номер не найден")
        return room