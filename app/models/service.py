from sqlalchemy import Boolean, Column, Float, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin

class Service(Base, TimestampMixin):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(Text)
    standard_fee = Column(Float)
    duration_days = Column(Integer)
    is_active = Column(Boolean, default=True)

    leads = relationship("Lead", back_populates="service")
    projects = relationship("Project", back_populates="service")
