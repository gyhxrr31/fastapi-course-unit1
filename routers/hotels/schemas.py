from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date


class BookingWithRoomResponse(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int
    rooms_left: int

    model_config = ConfigDict(from_attributes=True)

