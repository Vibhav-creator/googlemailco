"""Utilities for creating API routers with common dependencies."""

from typing import Iterable, List, Optional

from fastapi import APIRouter, Depends

from app.models.base import UserRole
from .auth import require_role


def router_factory(
    *,
    prefix: str = "",
    tags: Optional[List[str]] = None,
    roles: Optional[Iterable[UserRole]] = None,
) -> APIRouter:
    """Create an :class:`fastapi.APIRouter` with optional role enforcement.

    Parameters
    ----------
    prefix:
        Route prefix for the router.
    tags:
        Optional list of tags to apply to the router.
    roles:
        Optional iterable of :class:`~app.models.base.UserRole`. When provided,
        all routes registered on the router will require the authenticated user to
        possess one of these roles.
    """

    dependencies = []
    if roles:
        dependencies.append(Depends(require_role(*roles)))

    return APIRouter(prefix=prefix, tags=tags or [], dependencies=dependencies)
