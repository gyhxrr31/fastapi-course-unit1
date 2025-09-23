from pydantic import BaseModel, EmailStr, ConfigDict


class SUser(BaseModel):
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)