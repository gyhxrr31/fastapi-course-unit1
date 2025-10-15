from db.base_dao import BaseDAO
from db.db import async_session_maker
from models.bookings import Bookings
from models.rooms import Rooms
from sqlalchemy import select, or_, and_, func, insert, not_
from datetime import date


class BookingsDAO(BaseDAO):
    model = Bookings
    left_model = Rooms

    @classmethod
    async def check_rooms_left(
            cls,
            room_id: int,
            date_from: date,
            date_to: date,
    ):
        booked_rooms = (
            select(cls.model)
            .where(
                and_(
                    cls.model.room_id == room_id,
                    not_(
                        or_(
                            cls.model.date_to <= date_from,
                            cls.model.date_from >= date_to
                        )
                    )
                )
            )
            .cte("booked_rooms")
        )

        statement = select(
            (cls.left_model.quantity - func.count(booked_rooms.c.room_id)).label("rooms_left")
        ).select_from(cls.left_model).outerjoin(
            booked_rooms, booked_rooms.c.room_id == cls.left_model.id
        ).where(cls.left_model.id == room_id).group_by(
            cls.left_model.id, cls.left_model.quantity
        )

        async with async_session_maker() as session:
            rooms_left = await session.execute(statement)
            return rooms_left.scalar()

    @classmethod
    async def add_bookings(
            cls,
            user_id: int,
            room_id: int,
            date_from: date,
            date_to: date,
    ):
        rooms_left = await cls.check_rooms_left(
            user_id,
            room_id,
            date_from,
            date_to
        )
        if rooms_left > 0:
            async with async_session_maker() as session:
                get_price = select(cls.left_model.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price = price.scalar()
                add_booking = insert(cls.model).values(
                    room_id=room_id,
                    user_id=user_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price
                ).returning(cls.model)
                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
        else:
            return None
