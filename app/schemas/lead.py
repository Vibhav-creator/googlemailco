# This file is auto-generated. Do not edit manually.
from app.models.base import LeadStatus
from app.models.base import TaskPriority
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class LeadCreate(BaseModel):
    client_id: Optional[int] = None
    service_id: Optional[int] = None
    source: Optional[str] = None
    status: Optional[LeadStatus] = None
    probability: Optional[int] = None
    priority: Optional[TaskPriority] = None
    assigned_to_id: Optional[int] = None
    next_follow_up: Optional[datetime] = None
    estimated_value: Optional[float] = None

class LeadUpdate(BaseModel):
    client_id: Optional[int] = None
    service_id: Optional[int] = None
    source: Optional[str] = None
    status: Optional[LeadStatus] = None
    probability: Optional[int] = None
    priority: Optional[TaskPriority] = None
    assigned_to_id: Optional[int] = None
    next_follow_up: Optional[datetime] = None
    estimated_value: Optional[float] = None
