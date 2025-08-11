from fastapi import APIRouter, HTTPException, status, Response

from routers.users.schemas import SUserAuth
from routers.users.dao import UsersDAO
from routers.users.auth import get_password_hash, auth_user, create_jwt_token


router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register")
async def register_user(user_data: SUserAuth):
    existing_user = await UsersDAO.get_one_or_one(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This email already registered")
    hashed_password = await get_password_hash(user_data.password)
    await UsersDAO.insert_one(email=user_data.email, hashed_password=hashed_password)
    return {"msg":"Ok"}


@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await auth_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")
    access_token = await create_jwt_token({"sub":user.id})
    response.set_cookie("access_token", access_token, httponly=True)
    return access_token