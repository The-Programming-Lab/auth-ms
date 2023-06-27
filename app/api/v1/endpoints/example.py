from fastapi import APIRouter

from app.core.config import HELLO_WORLD
from app.core.database import db


router = APIRouter(prefix="/test", tags=["example"])


@router.get("/example")
async def example():
    user = db.collection("users").document("VcY55lmu0iHkdZ8AeqA5").get().to_dict()
    # example of John Doe
    print(user)
    return {"message": HELLO_WORLD, "user_name": user['fname']}