# This file is auto-generated. Do not edit manually.
from pydantic import BaseModel
from typing import Optional

class NotificationCreate(BaseModel):
    user_id: Optional[int] = None
    message: Optional[str] = None
    is_read: Optional[bool] = None
    link_to: Optional[str] = None
    notification_type: Optional[str] = None

class NotificationUpdate(BaseModel):
    user_id: Optional[int] = None
    message: Optional[str] = None
    is_read: Optional[bool] = None
    link_to: Optional[str] = None
    notification_type: Optional[str] = None
