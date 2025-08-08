# This file is auto-generated. Do not edit manually.
from datetime import date
from pydantic import BaseModel
from typing import Optional

class AgreementCreate(BaseModel):
    project_id: Optional[int] = None
    agreement_no: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    signed_date: Optional[date] = None
    file_url: Optional[str] = None
    termination_clause: Optional[str] = None
    is_active: Optional[bool] = None

class AgreementUpdate(BaseModel):
    project_id: Optional[int] = None
    agreement_no: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    signed_date: Optional[date] = None
    file_url: Optional[str] = None
    termination_clause: Optional[str] = None
    is_active: Optional[bool] = None
