from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.hotels import Base

class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    admin_role: Mapped[bool] = mapped_column(Boolean, server_default="False")
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    booking: Mapped["Bookings"] = relationship(
        "Bookings",
        back_populates="user",
    )


    def __str__(self):
        return self.email