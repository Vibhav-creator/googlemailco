# This file is auto-generated. Do not edit manually.
from datetime import date
from pydantic import BaseModel
from typing import Optional

class MilestoneCreate(BaseModel):
    project_id: Optional[int] = None
    name: Optional[str] = None
    target_date: Optional[date] = None
    completed_date: Optional[date] = None
    status: Optional[str] = None

class MilestoneUpdate(BaseModel):
    project_id: Optional[int] = None
    name: Optional[str] = None
    target_date: Optional[date] = None
    completed_date: Optional[date] = None
    status: Optional[str] = None
