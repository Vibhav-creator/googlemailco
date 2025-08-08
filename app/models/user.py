from sqlalchemy import Boolean, Column, DateTime, Integer, String, Enum
from sqlalchemy.orm import relationship, validates
from .base import Base, TimestampMixin, SoftDeleteMixin, UserRole
import re

class User(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password_hash = Column(String(128))
    full_name = Column(String(100))
    role = Column(Enum(UserRole), default=UserRole.USER)
    token_version = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime)

    assigned_leads = relationship("Lead", back_populates="assigned_to")
    tasks = relationship("Task", back_populates="assigned_to")
    notes = relationship("Note", back_populates="author")
    notifications = relationship("Notification", back_populates="user")

    @validates("email")
    def validate_email(self, key, email):
        if email and not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email address")
        return email
