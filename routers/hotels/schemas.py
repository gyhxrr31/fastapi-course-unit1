from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date


class BookingWithRoomResponse(BaseModel):
    id: int
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int
    # Данные номера
    room_name: str
    room_description: Optional[str]
    room_services: List[str]
    room_image_id: int

    model_config = ConfigDict(from_attributes=True)

