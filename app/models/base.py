from sqlalchemy import Column, Date, DateTime, Enum, Float, Integer, String, Text, Boolean, ForeignKey, UniqueConstraint, func
from sqlalchemy.orm import relationship, validates
from app.database import Base
import enum
import re

# Enums
class HospitalType(str, enum.Enum):
    SINGLE_SPECIALTY = "Single Specialty"
    MULTI_SPECIALTY = "Multi Specialty"
    CLINIC = "Clinic"
    DIAGNOSTIC_CENTER = "Diagnostic Center"
    HOSPITAL_CHAIN = "Hospital Chain"

class AccreditationStatus(str, enum.Enum):
    DRAFT = "Draft"
    IN_PROGRESS = "In Progress"
    ACCREDITED = "Accredited"
    REJECTED = "Rejected"
    RENEWAL_PENDING = "Renewal Pending"

class PaymentStatus(str, enum.Enum):
    PENDING = "Pending"
    PARTIAL = "Partial"
    PAID = "Paid"
    OVERDUE = "Overdue"
    REFUNDED = "Refunded"

class TaskPriority(str, enum.Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class LeadStatus(str, enum.Enum):
    NEW = "New"
    CONTACTED = "Contacted"
    QUALIFIED = "Qualified"
    PROPOSAL_SENT = "Proposal Sent"
    NEGOTIATION = "Negotiation"
    CONVERTED = "Converted"
    CLOSED_LOST = "Closed Lost"
    ON_HOLD = "On Hold"

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"

# Mixins
class TimestampMixin:
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class SoftDeleteMixin:
    is_deleted = Column(Boolean, default=False)

class ContactMixin:
    email = Column(String(120), index=True)
    phone = Column(String(20))
    whatsapp = Column(String(20))
    address = Column(Text)
    city = Column(String(50))
    state = Column(String(50))
    country = Column(String(50), default="India")
    postal_code = Column(String(15))

    @validates("phone", "whatsapp")
    def validate_phone(self, key, value):
        if value and not value.startswith("+"):
            raise ValueError("Phone number must start with '+'")
        return value
