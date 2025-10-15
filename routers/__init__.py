from fastapi import APIRouter
#routers
from routers.bookings.router import router as bookings_router
from routers.auth.router import router as auth_router
from routers.users.router import router as user_router
from routers.admin.router import router as admin_router
from routers.hotels.router import router as hotel_router
from routers.hotels.rooms.router import router as rooms_router
from pages.router import router as page_router
from images.router import router as images_router

router = APIRouter(
    prefix="/api/v1"
)


router.include_router(
    bookings_router,
    prefix="/bookings",
    tags=["Bookings"]
)


router.include_router(
    hotel_router,
    prefix="/hotels",
    tags=["Hotels"]
)


router.include_router(
    rooms_router,
    tags=["Rooms"]
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

upload_images_router = APIRouter(
    prefix="/images",
    tags=["Upload images router"]
)

upload_images_router.include_router(
    images_router,
    prefix="/images"
)

frontend_router = APIRouter(
    prefix="/pages"
)

frontend_router.include_router(
    page_router,
    tags=["Frontend | Pages"]
)


