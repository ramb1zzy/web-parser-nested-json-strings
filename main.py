from fastapi import FastAPI
from app.endpoints import router as serializer_router

app = FastAPI()

app.include_router(router=serializer_router, tags=["JSON Parser"])
