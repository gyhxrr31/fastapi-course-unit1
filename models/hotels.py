from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, JSON


class Base(DeclarativeBase):
    pass


class Hotels(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    location: Mapped[str] = mapped_column(String, nullable=False)
    services: Mapped[list] = mapped_column(JSON, nullable=True)
    rooms_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    image_id: Mapped[int] = mapped_column(Integer, nullable=True)

    room: Mapped["Rooms"] = relationship(
        "Rooms",
        back_populates="hotel",
        lazy="joined"
    )

    def __str__(self):
        return self.name