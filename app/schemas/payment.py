# This file is auto-generated. Do not edit manually.
from app.models.base import PaymentStatus
from datetime import date
from pydantic import BaseModel
from typing import Optional

class PaymentCreate(BaseModel):
    client_id: Optional[int] = None
    project_id: Optional[int] = None
    amount: Optional[float] = None
    due_date: Optional[date] = None
    paid_date: Optional[date] = None
    reference_no: Optional[str] = None
    status: Optional[PaymentStatus] = None
    payment_method: Optional[str] = None
    notes: Optional[str] = None

class PaymentUpdate(BaseModel):
    client_id: Optional[int] = None
    project_id: Optional[int] = None
    amount: Optional[float] = None
    due_date: Optional[date] = None
    paid_date: Optional[date] = None
    reference_no: Optional[str] = None
    status: Optional[PaymentStatus] = None
    payment_method: Optional[str] = None
    notes: Optional[str] = None
