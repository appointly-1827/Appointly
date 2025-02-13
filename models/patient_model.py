from sqlalchemy import Column, String, Integer, Boolean, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    patient_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    phone_number = Column(String(20), unique=True, nullable=False)
    otp = Column(String(6), nullable=False)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=True)
    email_id = Column(String(255), unique=True, nullable=True)
    address = Column(Text, nullable=True)
    location_access = Column(Boolean, default=True)
    preferred_clinic = Column(String(255), nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
