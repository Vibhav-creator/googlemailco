import logging

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.api import api_router
from app.database import Base, engine

logger = logging.getLogger(__name__)

app = FastAPI()


@app.on_event("startup")
async def validate_openapi_schema() -> None:
    """Generate the OpenAPI schema to ensure application routes are valid."""
    try:
        get_openapi(title=app.title, version=app.version, routes=app.routes)
    except Exception as exc:  # pragma: no cover - defensive programming
        logger.exception("Failed to generate OpenAPI schema")
        raise exc


# create database tables
Base.metadata.create_all(bind=engine)

app.include_router(api_router)
