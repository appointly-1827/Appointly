from sqlalchemy import Column, String, Integer, Boolean, Numeric, ForeignKey, LargeBinary
from sqlalchemy import Column, String, Integer, Boolean, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from database import Base
from sqlalchemy.orm import relationship
class Doctor(Base):
    __tablename__ = "doctors"
    dr_id = Column(String(255), primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)  # Changed to String
    doc_name = Column(String(255), nullable=False)
    phone_number = Column(Integer, unique=True, nullable=False)
    speciality = Column(String(255), nullable=False)
    year_of_experience = Column(Integer, nullable=True)
    estimated_patients = Column(Integer, nullable=True)
    available_time = Column(Boolean, default=True, nullable=False)
    license = Column(String, nullable=True)  # Use LargeBinary for bytea type
    consultation_fee = Column(Numeric(10, 2), nullable=True)
    clinic_id = Column(Integer, ForeignKey("clinic.clinic_id"), nullable=True)



    # Relationship with Clinic
    clinic = relationship("Clinic", back_populates="doctors")
