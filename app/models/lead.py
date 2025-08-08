from sqlalchemy import Column, DateTime, Enum, Float, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin, SoftDeleteMixin, LeadStatus, TaskPriority

class Lead(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "leads"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    source = Column(String(100))
    status = Column(Enum(LeadStatus), default=LeadStatus.NEW, index=True)
    probability = Column(Integer, default=30)
    priority = Column(Enum(TaskPriority), default=TaskPriority.MEDIUM)
    assigned_to_id = Column(Integer, ForeignKey("users.id"))
    next_follow_up = Column(DateTime, index=True)
    estimated_value = Column(Float)

    __table_args__ = (
        UniqueConstraint("client_id", "service_id", name="uq_lead_per_service_per_client"),
    )

    client = relationship("Client", back_populates="leads")
    service = relationship("Service", back_populates="leads")
    assigned_to = relationship("User", back_populates="assigned_leads")
    notes = relationship("Note", back_populates="lead")
    tasks = relationship("Task", back_populates="lead")
    documents = relationship("Document", back_populates="lead")
