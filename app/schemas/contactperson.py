# This file is auto-generated. Do not edit manually.
from pydantic import BaseModel
from typing import Optional

class ContactPersonCreate(BaseModel):
    client_id: Optional[int] = None
    name: Optional[str] = None
    designation: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    is_primary: Optional[bool] = None

class ContactPersonUpdate(BaseModel):
    client_id: Optional[int] = None
    name: Optional[str] = None
    designation: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    is_primary: Optional[bool] = None
