# This file is auto-generated. Do not edit manually.
from app.models.base import UserRole
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    full_name: Optional[str] = None
    role: Optional[UserRole] = None
    token_version: Optional[int] = None
    is_active: Optional[bool] = None
    last_login: Optional[datetime] = None

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    full_name: Optional[str] = None
    role: Optional[UserRole] = None
    token_version: Optional[int] = None
    is_active: Optional[bool] = None
    last_login: Optional[datetime] = None
