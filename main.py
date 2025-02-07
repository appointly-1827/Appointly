from sqlalchemy import UUID, create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models import Doctor
from schemas import DoctorResponse
from typing import List, Optional

# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

@app.get("/doctors", response_model=List[DoctorResponse])
def get_doctors(
    speciality: Optional[str] = None,  # Use Optional for optional parameters
    location: Optional[str] = None,  # Placeholder if location is to be added in the future
    search: Optional[str] = None,  # Optional search
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    query = db.query(Doctor)
    
    # Apply filtering based on parameters
    if speciality:
        query = query.filter(Doctor.speciality.ilike(f"%{speciality}%"))
    if search:
        query = query.filter(Doctor.doc_name.ilike(f"%{search}%"))
    if location:  # Location filter placeholder (no functionality yet)
        query = query.filter(Doctor.clinic_id == location)  # Assuming location is linked to clinic_id

    doctors = query.offset(offset).limit(limit).all()
    return doctors

@app.get("/doctors/{doctor_id}", response_model=DoctorResponse)
def get_doctor_details(doctor_id: str, db: Session = Depends(get_db)):
    # Ensure that the doctor_id is properly matched as a string
    doctor = db.query(Doctor).filter(Doctor.dr_id == doctor_id).first()
    
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    return doctor
@app.post("/")
def create_doctor(doctor: DoctorResponse, db: Session = Depends(get_db)):
    # Create the doctor object
    db_doctor = Doctor(
        doc_name=doctor.doc_name,
        phone_number=doctor.phone_number,
        speciality=doctor.speciality,
        year_of_experience=doctor.year_of_experience,
        estimated_patients=doctor.estimated_patients,
        available_time=doctor.available_time,
        license=doctor.license,
        consultation_fee=doctor.consultation_fee,
        clinic_id=doctor.clinic_id,
    )
    
    # Add doctor to the database
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    
    return {"message": "Doctor created successfully", "doctor_id": db_doctor.dr_id}
