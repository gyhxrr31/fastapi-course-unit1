from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Date, ForeignKey, Computed
from datetime import date

from models.hotels import Base



class Bookings(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date] = mapped_column(Date, nullable=False)
    date_to: Mapped[date] = mapped_column(Date, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    total_cost: Mapped[int] = mapped_column(Integer, Computed("(date_to - date_from) * price")) #Попробовать тут формулу "(total_cost * total_days)"
    total_days: Mapped[int] = mapped_column(Integer, Computed("(date_to - date_from)"))