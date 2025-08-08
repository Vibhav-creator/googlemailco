from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship
from .base import Base, ContactMixin, TimestampMixin, SoftDeleteMixin, HospitalType

class Client(Base, ContactMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    hospital_name = Column(String(200))
    beds = Column(Integer)
    hospital_type = Column(Enum(HospitalType))
    director_name = Column(String(100))
    website = Column(String(200))
    is_active = Column(Boolean, default=True)

    projects = relationship("Project", back_populates="client", cascade="all, delete-orphan")
    leads = relationship("Lead", back_populates="client", cascade="all, delete-orphan")
    payments = relationship("Payment", back_populates="client", cascade="all, delete-orphan")
    contacts = relationship("ContactPerson", back_populates="client", cascade="all, delete-orphan")
    documents = relationship("Document", back_populates="client")

class ContactPerson(Base, TimestampMixin):
    __tablename__ = "contact_persons"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    name = Column(String(100))
    designation = Column(String(100))
    email = Column(String(120))
    phone = Column(String(20))
    is_primary = Column(Boolean, default=False)

    client = relationship("Client", back_populates="contacts")
