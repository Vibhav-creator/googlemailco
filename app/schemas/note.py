# This file is auto-generated. Do not edit manually.
from pydantic import BaseModel
from typing import Optional

class NoteCreate(BaseModel):
    content: Optional[str] = None
    author_id: Optional[int] = None
    lead_id: Optional[int] = None
    project_id: Optional[int] = None

class NoteUpdate(BaseModel):
    content: Optional[str] = None
    author_id: Optional[int] = None
    lead_id: Optional[int] = None
    project_id: Optional[int] = None
