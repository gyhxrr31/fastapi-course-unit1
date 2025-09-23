from routers.auth.depends import decode_token, compare_exp_time
from fastapi import Depends
from routers.users.dao import UsersDAO


async def get_user_from_sub(
        token: dict = Depends(decode_token),
        expire_check: bool = Depends(compare_exp_time)
) -> list:
    sub_id = token.get("sub")
    return await UsersDAO.find_by_id(int(sub_id))