from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


from db.db import  engine
from routers.__init__ import router as api_router
from routers.__init__ import frontend_router
from routers.__init__ import upload_images_router


from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from admin.auth import AdminAuth

from admin.views import UsersView, BookingsView, RoomsView, HotelView

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from config import env_config

import uvicorn

@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url(
        url=env_config.REDIS_URL,
        encoding="utf-8",
        decode_responses=False
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(
    title="API V1",
    lifespan=lifespan
)


app.include_router(api_router)
app.include_router(frontend_router)
app.include_router(upload_images_router)
app.mount(path="/statics", app=StaticFiles(directory="statics"), name="statics")
authentication_backend = AdminAuth(secret_key=env_config.PRIVATE_KEY)
admin = Admin(app, engine=engine, base_url="/admin/panel", authentication_backend=authentication_backend)

admin.add_view(UsersView)
admin.add_view(BookingsView)
admin.add_view(RoomsView)
admin.add_view(HotelView)


app.add_middleware(
    CORSMiddleware,
    allow_origins=env_config.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)