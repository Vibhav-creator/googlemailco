# This file is auto-generated. Do not edit manually.
from app.models.base import TaskPriority
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[TaskPriority] = None
    status: Optional[str] = None
    assigned_to_id: Optional[int] = None
    lead_id: Optional[int] = None
    project_id: Optional[int] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    priority: Optional[TaskPriority] = None
    status: Optional[str] = None
    assigned_to_id: Optional[int] = None
    lead_id: Optional[int] = None
    project_id: Optional[int] = None
