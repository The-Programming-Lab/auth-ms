from fastapi import APIRouter
from app.api.config import base_path, hello_world

router = APIRouter(prefix=base_path, tags=["example"])


@router.get("/example")
async def example():
    return {"message": hello_world}