from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin

class Note(Base, TimestampMixin):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    lead_id = Column(Integer, ForeignKey("leads.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    author = relationship("User", back_populates="notes")
    lead = relationship("Lead", back_populates="notes")
    project = relationship("Project")
