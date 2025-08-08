from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin, PaymentStatus

class Payment(Base, TimestampMixin):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"), index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), index=True)
    amount = Column(Float)
    due_date = Column(Date)
    paid_date = Column(Date)
    reference_no = Column(String(100))
    status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    payment_method = Column(String(50))
    notes = Column(Text)

    client = relationship("Client", back_populates="payments")
    project = relationship("Project", back_populates="payments")
