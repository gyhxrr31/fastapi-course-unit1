from db.base_dao import BaseDAO
from models.bookings import Bookings


class BookingsDAO(BaseDAO):
    model = Bookings