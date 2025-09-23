from fastapi import APIRouter, Depends
from routers.users.depends import get_user_from_sub
from routers.users.schemas import SUser

router = APIRouter()


@router.get("/me")
async def about_current_user(current_user: SUser = Depends(get_user_from_sub)) -> SUser:
    return current_user