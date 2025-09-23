from fastapi import APIRouter, Response, Depends
from routers.auth.exceptions import EmailAlreadyRegisteredException, CredsInvalidException
from routers.auth.schemas import SUserAuth
from routers.auth.dao import AuthDAO
from routers.auth.auth import get_password_hash, auth_user, create_jwt_token


router = APIRouter()


@router.post("/register")
async def register_user(user_data: SUserAuth) -> dict:
    existing_user = await AuthDAO.get_one_or_none(email=user_data.email)
    if existing_user:
        raise EmailAlreadyRegisteredException
    hashed_password = await get_password_hash(user_data.password)
    await AuthDAO.insert_one(email=user_data.email, hashed_password=hashed_password)
    return {"msg":"Ok"}


@router.post("/login")
async def login_user(
        response: Response,
        user_data: SUserAuth) -> str:
    user = await auth_user(user_data.email, user_data.password)
    if not user:
        raise CredsInvalidException
    access_token = await create_jwt_token({"sub":str(user.id)})
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True
    )
    return access_token


@router.delete("/logout")
async def logout_user(response: Response) -> None:
    response.delete_cookie("access_token")
    return None