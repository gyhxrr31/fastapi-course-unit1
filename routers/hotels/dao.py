from db.base_dao import BaseDAO
from db.db import async_session_maker
from sqlalchemy import select, and_, or_,  not_, func
from models.rooms import Rooms
from models.hotels import Hotels
from models.bookings import Bookings
from datetime import date


class HotelDAO(BaseDAO):
    model = Hotels

    @classmethod
    async def find_hotels_with_available_rooms(
            cls,
            location: str,
            date_from: date,
            date_to: date,
    ):

        booked_rooms = (
            select(
                Rooms.hotel_id,
                func.count(Bookings.id).label("total_booked")
            )
            .select_from(Bookings)
            .join(Rooms, Bookings.room_id == Rooms.id)
            .where(
                not_(
                    or_(
                        Bookings.date_to <= date_from,
                        Bookings.date_from >= date_to
                    )
                )
            )
            .group_by(Rooms.hotel_id)
            .cte("booked_rooms")
        )

        # Основной запрос
        query = (
            select(
                Hotels.id,
                Hotels.name,
                Hotels.location,
                Hotels.services,
                Hotels.rooms_quantity,
                Hotels.image_id,
                (Hotels.rooms_quantity - func.coalesce(booked_rooms.c.total_booked, 0)).label("rooms_left")
            )
            .select_from(Hotels)
            .outerjoin(booked_rooms, Hotels.id == booked_rooms.c.hotel_id)
            .where(
                and_(
                    Hotels.location.ilike(f"%{location}%"),
                    Hotels.rooms_quantity > func.coalesce(booked_rooms.c.total_booked, 0)
                )
            )
            .order_by(Hotels.name)
        )

        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.mappings().all()