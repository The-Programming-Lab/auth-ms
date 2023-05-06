from fastapi import FastAPI

from app.api.v1.router import router
from app.core.config import BASE_PATH


app = FastAPI(docs_url=BASE_PATH + "/docs", openapi_url=BASE_PATH + "/openapi.json")

# add router from api/endpoints/example.py
app.include_router(router)


@app.get("/")
async def health_check():
    return "ok" 