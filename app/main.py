from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
import os

from app.api.v1.router import router
from app.core.logging import logger

if os.getenv("BASE_PATH") is None:
    os.environ["BASE_PATH"] = ""
    logger.critical("BASE_PATH is not set, setting to empty string")


app = FastAPI(docs_url=os.getenv("BASE_PATH") + "/docs", openapi_url=os.getenv("BASE_PATH") + "/openapi.json") # type: ignore

app.include_router(router)

@app.get("/")
async def health_check():
    return "ok" 