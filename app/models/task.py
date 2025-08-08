from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin, TaskPriority

class Task(Base, TimestampMixin):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    description = Column(Text)
    due_date = Column(DateTime)
    priority = Column(Enum(TaskPriority), default=TaskPriority.MEDIUM)
    status = Column(String(20), default="Pending")
    assigned_to_id = Column(Integer, ForeignKey("users.id"))
    lead_id = Column(Integer, ForeignKey("leads.id"))
    project_id = Column(Integer, ForeignKey("projects.id"))

    assigned_to = relationship("User", back_populates="tasks")
    lead = relationship("Lead", back_populates="tasks")
    project = relationship("Project", back_populates="tasks")
