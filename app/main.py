from fastapi import FastAPI
from app.api.endpoints import example
from app.api.config import health_check_endpoint

app = FastAPI()

# add router from api/endpoints/example.py
app.include_router(example.router)



@app.get(health_check_endpoint)
async def test():
    return "Ok"