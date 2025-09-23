from fastapi import FastAPI
from routers.__init__ import router as api_router

import uvicorn

app = FastAPI(title="API V1")

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)