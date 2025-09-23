from fastapi import Depends, Request
from jose.jwt import decode
from jose import JWTError
from config import env_config
from datetime import datetime, UTC
from routers.auth.exceptions import no_token_found_exception, token_validate_exception, expire_token_exception


async def get_token(request: Request) -> str:
    try:
        return request.cookies["access_token"]
    except KeyError:
        raise no_token_found_exception


async def decode_token(token: str = Depends(get_token)) -> dict:
    try:
        return decode(token, env_config.PRIVATE_KEY, env_config.ALGORITHM)
    except JWTError:
        raise token_validate_exception


async def compare_exp_time(token: dict = Depends(decode_token)) -> bool:
    if datetime.now(UTC).timestamp() >= token["exp"]:
        raise expire_token_exception
    return True