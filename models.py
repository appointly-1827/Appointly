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


from sqlalchemy import Column, String, Integer, Boolean, Numeric, ForeignKey, LargeBinary

class Doctor(Base):
    __tablename__ = "doctors"
    dr_id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)  # Changed to String
    doc_name = Column(String(255), nullable=False)
    phone_number = Column(Integer, unique=True, nullable=False)
    speciality = Column(String(255), nullable=False)
    year_of_experience = Column(Integer, nullable=True)
    estimated_patients = Column(Integer, nullable=True)
    available_time = Column(Boolean, default=True, nullable=False)
    license = Column(String(255), nullable=True)  # Use LargeBinary for bytea type
    consultation_fee = Column(Numeric(10, 2), nullable=True)
    clinic_id = Column(Integer, ForeignKey("clinic.clinic_id"), nullable=True)



class Clinic(Base):
    __tablename__ = "clinic"

    clinic_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    clinic_name = Column(String(255), nullable=False)
    clinic_address = Column(String(255), nullable=False)
    clinic_area = Column(String(255), nullable=False)
