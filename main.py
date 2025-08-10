from fastapi import FastAPI
from routers.bookings.router import router as bookings_router

import uvicorn

app = FastAPI()

app.include_router(bookings_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)