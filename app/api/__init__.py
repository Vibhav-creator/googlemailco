from __future__ import annotations

from fastapi import APIRouter

from app import schemas
from app.crud import get_crud
from app.models import (
    Client,
    Document,
    Lead,
    Note,
    Notification,
    Payment,
    Project,
    Service,
    Task,
    User,
)

from .factory import generate_router
from .auth import router as auth_router

MODELS = [
    User,
    Client,
    Lead,
    Project,
    Payment,
    Service,
    Document,
    Task,
    Note,
    Notification,
]

api_router = APIRouter()

# authentication routes
api_router.include_router(auth_router)

for m in MODELS:
    crud = get_crud(m)
    schema_read = getattr(schemas, f"{m.__name__}Read")
    schema_create = getattr(schemas, f"{m.__name__}Create")
    schema_update = getattr(schemas, f"{m.__name__}Update")
    api_router.include_router(
        generate_router(m.__name__, crud, schema_read, schema_create, schema_update)
    )

__all__ = ["api_router"]
