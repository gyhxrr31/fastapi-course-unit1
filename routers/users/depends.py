from fastapi import Depends, Request
from jose.jwt import decode
from jose import JWTError
from config import pwdconfig
from datetime import datetime, UTC
from routers.users.dao import UsersDAO
from routers.users.exceptions import no_token_found_exception, token_validate_exception, expire_token_exception


async def get_token(request: Request) -> str:
    try:
        return request.cookies["access_token"]
    except KeyError:
        raise no_token_found_exception


async def decode_token(token: str = Depends(get_token)) -> dict:
    try:
        return decode(token, pwdconfig.PRIVATE_KEY, pwdconfig.ALGORITHM)
    except JWTError:
        raise token_validate_exception


async def compare_exp_time(token: dict = Depends(decode_token)) -> bool:
    if datetime.now(UTC).timestamp() >= token["exp"]:
        raise expire_token_exception
    return True


async def get_user_from_sub(
        token: dict = Depends(decode_token),
        expire_check: bool = Depends(compare_exp_time)
) -> list:
    sub_id = token.get("sub")
    return await UsersDAO.find_by_id(int(sub_id))
