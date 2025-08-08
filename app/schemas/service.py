# This file is auto-generated. Do not edit manually.
from pydantic import BaseModel
from typing import Optional

class ServiceCreate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    standard_fee: Optional[float] = None
    duration_days: Optional[int] = None
    is_active: Optional[bool] = None

class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    standard_fee: Optional[float] = None
    duration_days: Optional[int] = None
    is_active: Optional[bool] = None
