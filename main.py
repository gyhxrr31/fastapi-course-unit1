from fastapi import FastAPI
#routers
from routers.bookings.router import router as bookings_router
from routers.auth.router import router as auth_router
from routers.users.router import router as user_router

import uvicorn

app = FastAPI()

app.include_router(bookings_router)
app.include_router(auth_router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)