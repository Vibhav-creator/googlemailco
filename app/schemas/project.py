# This file is auto-generated. Do not edit manually.
from app.models.base import AccreditationStatus
from datetime import date
from pydantic import BaseModel
from typing import Optional

class ProjectCreate(BaseModel):
    client_id: Optional[int] = None
    service_id: Optional[int] = None
    title: Optional[str] = None
    status: Optional[AccreditationStatus] = None
    start_date: Optional[date] = None
    target_date: Optional[date] = None
    completed_date: Optional[date] = None
    expected_fee: Optional[float] = None
    actual_fee: Optional[float] = None

class ProjectUpdate(BaseModel):
    client_id: Optional[int] = None
    service_id: Optional[int] = None
    title: Optional[str] = None
    status: Optional[AccreditationStatus] = None
    start_date: Optional[date] = None
    target_date: Optional[date] = None
    completed_date: Optional[date] = None
    expected_fee: Optional[float] = None
    actual_fee: Optional[float] = None
