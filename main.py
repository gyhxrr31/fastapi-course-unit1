from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers.__init__ import router as api_router
from routers.__init__ import frontend_router
from routers.__init__ import upload_images_router
from config import env_config

import uvicorn

app = FastAPI(title="API V1")

app.include_router(api_router)
app.include_router(frontend_router)
app.include_router(upload_images_router)
app.mount(path="/statics", app=StaticFiles(directory="statics"), name="statics")

app.add_middleware(
    CORSMiddleware,
    allow_origins=env_config.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)