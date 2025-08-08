# This file is auto-generated. Do not edit manually.
from pydantic import BaseModel
from typing import Optional

class DocumentCreate(BaseModel):
    client_id: Optional[int] = None
    lead_id: Optional[int] = None
    project_id: Optional[int] = None
    name: Optional[str] = None
    document_type: Optional[str] = None
    file_url: Optional[str] = None
    uploaded_by_id: Optional[int] = None

class DocumentUpdate(BaseModel):
    client_id: Optional[int] = None
    lead_id: Optional[int] = None
    project_id: Optional[int] = None
    name: Optional[str] = None
    document_type: Optional[str] = None
    file_url: Optional[str] = None
    uploaded_by_id: Optional[int] = None
