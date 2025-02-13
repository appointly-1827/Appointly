from sqlalchemy import Column, String, Integer, Boolean, Text, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid
from database import Base
from sqlalchemy.orm import relationship

class Clinic(Base):
    __tablename__ = "clinic"

    clinic_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    clinic_name = Column(String(255), nullable=False)
    clinic_address = Column(String(255), nullable=False)
    clinic_area = Column(String(255), nullable=False)
    doctors = relationship("Doctor", back_populates="clinic", cascade="all, delete")