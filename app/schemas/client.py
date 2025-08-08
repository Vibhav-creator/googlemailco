# This file is auto-generated. Do not edit manually.
from app.models.base import HospitalType
from pydantic import BaseModel
from typing import Optional

class ClientCreate(BaseModel):
    name: Optional[str] = None
    hospital_name: Optional[str] = None
    beds: Optional[int] = None
    hospital_type: Optional[HospitalType] = None
    director_name: Optional[str] = None
    website: Optional[str] = None
    is_active: Optional[bool] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    whatsapp: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    hospital_name: Optional[str] = None
    beds: Optional[int] = None
    hospital_type: Optional[HospitalType] = None
    director_name: Optional[str] = None
    website: Optional[str] = None
    is_active: Optional[bool] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    whatsapp: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
