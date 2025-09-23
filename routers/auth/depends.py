from fastapi import Depends, Request
from jose.jwt import decode
from jose import JWTError
from config import env_config
from datetime import datetime, UTC
from routers.auth.exceptions import TokenAbsentException, TokenValidateException, ExpireTokenException


async def get_token(request: Request) -> str:
    try:
        return request.cookies["access_token"]
    except KeyError:
        raise TokenAbsentException


async def decode_token(token: str = Depends(get_token)) -> dict:
    try:
        return decode(token, env_config.PRIVATE_KEY, env_config.ALGORITHM)
    except JWTError:
        raise TokenValidateException


async def compare_exp_time(token: dict = Depends(decode_token)) -> bool:
    if datetime.now(UTC).timestamp() >= token["exp"]:
        raise ExpireTokenException
    return True