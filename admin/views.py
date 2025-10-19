from models.bookings import Bookings
from models.users import Users
from models.hotels import Hotels
from models.rooms import Rooms
from sqladmin import ModelView



class BookingsView(ModelView, model=Bookings):
    name = "Booking"
    name_plural = "Bookings"
    column_list = [Bookings.id, Bookings.user, Bookings.room_id, Bookings.user_id, Bookings.date_from, Bookings.date_to]
    column_searchable_list = [Bookings.id]
    column_details_exclude_list = None


class UsersView(ModelView, model=Users):
    name = "User"
    name_plural = "Users"
    column_details_exclude_list = [Users.hashed_password]
    column_list = [Users.id, Users.booking, Users.email, Users.admin_role]


class RoomsView(ModelView, model=Rooms):
    name = "Room"
    name_plural = "Rooms"
    column_list = [Rooms.hotel] + [c for c in Rooms.__table__.columns]


class HotelView(ModelView, model=Hotels):
    name = "Hotel"
    name_plural = "Hotels"
    column_list = [Hotels.room] + [c for c in Hotels.__table__.columns]