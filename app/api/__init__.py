"""API package providing dependencies and router utilities."""

from .auth import require_role
from .router import router_factory

__all__ = ["require_role", "router_factory"]
