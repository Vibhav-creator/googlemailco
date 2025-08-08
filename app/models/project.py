from sqlalchemy import Column, Date, Enum, Float, ForeignKey, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin, SoftDeleteMixin, AccreditationStatus

class Project(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    title = Column(String(200))
    status = Column(Enum(AccreditationStatus), default=AccreditationStatus.DRAFT)
    start_date = Column(Date)
    target_date = Column(Date)
    completed_date = Column(Date)
    expected_fee = Column(Float)
    actual_fee = Column(Float)

    client = relationship("Client", back_populates="projects")
    service = relationship("Service", back_populates="projects")
    quotes = relationship("Quote", back_populates="project", cascade="all, delete-orphan")
    agreements = relationship("Agreement", back_populates="project", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="project")
    milestones = relationship("Milestone", back_populates="project")
    payments = relationship("Payment", back_populates="project", lazy="selectin")

class Quote(Base, TimestampMixin):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    version = Column(Integer, default=1)
    quote_no = Column(String(50), unique=True)
    amount = Column(Float)
    discount_pct = Column(Float)
    valid_until = Column(Date)
    terms = Column(Text)
    is_accepted = Column(Boolean, default=False)

    project = relationship("Project", back_populates="quotes")

class Agreement(Base, TimestampMixin):
    __tablename__ = "agreements"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    agreement_no = Column(String(50), unique=True)
    start_date = Column(Date)
    end_date = Column(Date)
    signed_date = Column(Date)
    file_url = Column(String(400))
    termination_clause = Column(Text)
    is_active = Column(Boolean, default=True)

    project = relationship("Project", back_populates="agreements")

class Milestone(Base, TimestampMixin):
    __tablename__ = "milestones"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    name = Column(String(150))
    target_date = Column(Date)
    completed_date = Column(Date)
    status = Column(String(30), default="Pending")

    project = relationship("Project", back_populates="milestones")
