from passlib.context import CryptContext
from datetime import timedelta, datetime, UTC
from jose import jwt
from pydantic import EmailStr
from routers.users.dao import UsersDAO
from config import env_config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


async def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


async def create_jwt_token(data: dict) -> str:
    to_encode = data.copy()
    expire_at = datetime.now(UTC) + timedelta(minutes=30)
    to_encode.update({"exp":expire_at})
    encoded_jwt = jwt.encode(
        to_encode, env_config.PRIVATE_KEY, env_config.ALGORITHM
    )
    return encoded_jwt


async def auth_user(email: EmailStr, password: str):
    user = await UsersDAO.get_one_or_none(email=email)
    if not user:
        return None

    if not await verify_password(password, user.hashed_password):
        return None

    return user