from fastapi import APIRouter, Depends
from routers.admin.dao import AdminDAO
from routers.admin.depends import check_current_user
from routers.admin.schemas import AdminUserList

router = APIRouter()


@router.get("/users")
async def get_users(
        current_user: str = Depends(check_current_user)
) -> list[AdminUserList]:
    return await AdminDAO.select_all()