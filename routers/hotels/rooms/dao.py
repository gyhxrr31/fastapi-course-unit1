from db.base_dao import BaseDAO
from db.db import async_session_maker
from models.rooms import Rooms
from models.hotels import Hotels
from models.bookings import Bookings
from sqlalchemy import select, and_, not_, or_
from datetime import date


class RoomDAO(BaseDAO):
    model = Rooms


    @classmethod
    async def find_available_rooms_by_hotel(
            cls,
            hotel_id: int,
            date_from: date,
            date_to: date,
    ):
        """
        Находит свободные номера в конкретном отеле на указанные даты
        """
        # CTE для забронированных номеров
        booked_rooms = (
            select(Bookings.room_id)
            .where(
                not_(
                    or_(
                        Bookings.date_to <= date_from,
                        Bookings.date_from >= date_to
                    )
                )
            )
            .cte("booked_rooms")
        )

        query = (
            select(
                Rooms.id,
                Rooms.hotel_id,
                Rooms.name,
                Rooms.description,
                Rooms.price,
                Rooms.services,
                Rooms.quantity,
                Rooms.image_id,
                # Можно добавить информацию об отеле
                Hotels.name.label("hotel_name"),
                Hotels.location.label("hotel_location")
            )
            .select_from(Rooms)
            .join(Hotels, Rooms.hotel_id == Hotels.id)
            .where(
                and_(
                    Rooms.hotel_id == hotel_id,
                    Rooms.id.not_in(select(booked_rooms.c.room_id))
                )
            )
            .order_by(Rooms.price)
        )

        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_all_by_hotel_id(cls, hotel_id: int):
        """
        Находит все номера отеля (без учета бронирований)
        """
        query = (
            select(Rooms)
            .where(Rooms.hotel_id == hotel_id)
            .order_by(Rooms.price)
        )

        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def get_room_with_hotel_info(cls, room_id: int):
        """
        Получает информацию о номере с данными об отеле
        """
        query = (
            select(
                Rooms,
                Hotels.name.label("hotel_name"),
                Hotels.location.label("hotel_location"),
                Hotels.services.label("hotel_services")
            )
            .select_from(Rooms)
            .join(Hotels, Rooms.hotel_id == Hotels.id)
            .where(Rooms.id == room_id)
        )

        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.mappings().first()