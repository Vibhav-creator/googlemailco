from fastapi import FastAPI

from app.api import api_router
from app.database import Base, engine

app = FastAPI()

# create database tables
Base.metadata.create_all(bind=engine)

# simple health/root endpoint
@app.get("/")
async def read_root():
    return {"message": "Hospital CRM API"}

app.include_router(api_router)
