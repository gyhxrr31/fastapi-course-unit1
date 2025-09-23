from fastapi import Depends
from routers.users.depends import get_user_from_sub
from models.users import Users
from routers.admin.exceptions import RestrictedAccessException


async def check_current_user(
        current_user: Users = Depends(get_user_from_sub)
) -> bool:
    if current_user.admin_role:
        return True
    raise RestrictedAccessException