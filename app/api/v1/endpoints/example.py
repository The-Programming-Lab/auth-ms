from fastapi import APIRouter

from app.core.config import HELLO_WORLD


router = APIRouter(prefix="/test", tags=["example"])


@router.get("/example")
async def example():
    return {"message": HELLO_WORLD}