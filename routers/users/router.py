from urllib.request import Request

from fastapi import APIRouter, Response
from routers.users.exceptions import email_already_registered_exception, creds_invalid_exception
from routers.users.schemas import SUserAuth
from routers.users.dao import UsersDAO
from routers.users.auth import get_password_hash, auth_user, create_jwt_token


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth) -> dict:
    existing_user = await UsersDAO.get_one_or_one(email=user_data.email)
    if existing_user:
        raise email_already_registered_exception
    hashed_password = await get_password_hash(user_data.password)
    await UsersDAO.insert_one(email=user_data.email, hashed_password=hashed_password)
    return {"msg":"Ok"}


@router.post("/login")
async def login_user(
        response: Response,
        user_data: SUserAuth) -> str:
    user = await auth_user(user_data.email, user_data.password)
    if not user:
        raise creds_invalid_exception
    access_token = await create_jwt_token({"sub":str(user.id)})
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True
    )
    return access_token


@router.delete("/logout")
async def logout_user(response: Response):
    response.delete_cookie("access_token")
    return None
