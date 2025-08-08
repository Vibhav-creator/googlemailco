from __future__ import annotations

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

from .factory import create_schemas

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

for m in MODELS:
    create, read, update = create_schemas(m)
    globals()[f"{m.__name__}Create"] = create
    globals()[f"{m.__name__}Read"] = read
    globals()[f"{m.__name__}Update"] = update

__all__ = []
for m in MODELS:
    __all__.extend(
        [f"{m.__name__}Create", f"{m.__name__}Read", f"{m.__name__}Update"]
    )

# authentication schemas
from .auth import Token

__all__.append("Token")
