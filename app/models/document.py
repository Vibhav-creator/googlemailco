from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin

class Document(Base, TimestampMixin):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    lead_id = Column(Integer, ForeignKey("leads.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))
    name = Column(String(200))
    document_type = Column(String(50))
    file_url = Column(String(400))
    uploaded_by_id = Column(Integer, ForeignKey("users.id"))

    client = relationship("Client", back_populates="documents")
    lead = relationship("Lead", back_populates="documents")
    uploaded_by = relationship("User")
