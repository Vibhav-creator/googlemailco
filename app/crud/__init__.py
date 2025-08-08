from __future__ import annotations

from typing import Dict, Type

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

from .base import CRUDBase

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

crud_map: Dict[str, CRUDBase] = {m.__name__: CRUDBase(m) for m in MODELS}


def get_crud(model: Type) -> CRUDBase:
    """Return CRUD instance for a given model class."""
    return crud_map[model.__name__]


# Expose CRUD instances as module-level variables for convenience
for _model in MODELS:
    globals()[_model.__name__.lower()] = crud_map[_model.__name__]

__all__ = [m.__name__.lower() for m in MODELS] + ["get_crud"]
