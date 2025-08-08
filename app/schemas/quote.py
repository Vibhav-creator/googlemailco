# This file is auto-generated. Do not edit manually.
from datetime import date
from pydantic import BaseModel
from typing import Optional

class QuoteCreate(BaseModel):
    project_id: Optional[int] = None
    version: Optional[int] = None
    quote_no: Optional[str] = None
    amount: Optional[float] = None
    discount_pct: Optional[float] = None
    valid_until: Optional[date] = None
    terms: Optional[str] = None
    is_accepted: Optional[bool] = None

class QuoteUpdate(BaseModel):
    project_id: Optional[int] = None
    version: Optional[int] = None
    quote_no: Optional[str] = None
    amount: Optional[float] = None
    discount_pct: Optional[float] = None
    valid_until: Optional[date] = None
    terms: Optional[str] = None
    is_accepted: Optional[bool] = None
