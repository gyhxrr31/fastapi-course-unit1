from fastapi import APIRouter
#routers
from routers.bookings.router import router as bookings_router
from routers.auth.router import router as auth_router
from routers.users.router import router as user_router
from routers.admin.router import router as admin_router


router = APIRouter(
    prefix="/api/v1"
)


router.include_router(
    bookings_router,
    prefix="/bookings",
    tags=["Bookings"]
)

router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Auth"]

)

router.include_router(
    user_router,
    prefix="/users",
    tags=["Users"]
)


router.include_router(
    admin_router,
    prefix="/admin",
    tags=["Admin"]
)