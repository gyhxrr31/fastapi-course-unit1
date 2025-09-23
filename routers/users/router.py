from fastapi import APIRouter, Depends
from routers.users.depends import get_user_from_sub
from models.users import Users

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/me")
async def about_current_user(current_user: Users = Depends(get_user_from_sub)):
    return current_user

