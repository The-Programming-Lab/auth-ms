from fastapi import APIRouter
import os

from app.core.config import BASE_PATH
from app.api.v1.endpoints import example


router = APIRouter(prefix=BASE_PATH)

router.include_router(example.router)
