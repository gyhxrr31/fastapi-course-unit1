from pydantic import BaseModel, ConfigDict, computed_field
from typing import Optional, List
from datetime import date


class RoomWithAvailabilityResponse(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: Optional[str]
    services: List[str]
    price: int
    quantity: int
    image_id: int
    rooms_left: int

    @computed_field
    @property
    def total_cost(
            self,
            date_from: date,
            date_to: date
    ) -> int:
        days = (date_to - date_from).days
        return self.price * days

    model_config = ConfigDict(from_attributes=True)