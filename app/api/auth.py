"""Authentication dependencies for API routes."""

from typing import Iterable

from fastapi import Depends, HTTPException, status

from app.models.user import User
from app.models.base import UserRole


async def require_user() -> User:  # pragma: no cover - placeholder
    """Retrieve the currently authenticated user.

    This is a stub to be replaced with the project's actual authentication
    mechanism. It raises ``HTTPException`` to indicate that authentication is
    required.
    """
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
    )


def require_role(*roles: Iterable[UserRole]):
    """Return a dependency ensuring the current user has one of ``roles``.

    Parameters
    ----------
    *roles:
        Allowed :class:`~app.models.base.UserRole` values. At least one role must
        match the authenticated user's role for the request to proceed.
    """

    async def dependency(user: User = Depends(require_user)) -> User:
        if roles and user.role not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions",
            )
        return user

    return dependency
