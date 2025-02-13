from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from models.clinic_model import Clinic
from models.doctor_model import Doctor
from schemas import ClinicResponse, ClinicCreate, DoctorResponse

router = APIRouter(prefix="/clinics", tags=["Clinics"])

# Get all clinics
@router.get("/", response_model=List[ClinicResponse])
def get_clinics(db: Session = Depends(get_db)):
    clinics = db.query(Clinic).all()
    return clinics

# Get details of a specific clinic
@router.get("/{clinic_id}", response_model=ClinicResponse)
def get_clinic_details(clinic_id: int, db: Session = Depends(get_db)):
    clinic = db.query(Clinic).filter(Clinic.clinic_id == clinic_id).first()
    
    if not clinic:
        raise HTTPException(status_code=404, detail="Clinic not found")
    
    return clinic

# Add a new clinic
@router.post("/add", response_model=ClinicResponse)
def create_clinic(clinic: ClinicCreate, db: Session = Depends(get_db)):
    db_clinic = Clinic(
        clinic_name=clinic.clinic_name,
        clinic_address=clinic.clinic_address,
        clinic_area=clinic.clinic_area,
    )

    db.add(db_clinic)
    db.commit()
    db.refresh(db_clinic)

    return db_clinic


import base64
def convert_license_to_string(license_data):
    if isinstance(license_data, memoryview):  # Convert memoryview to bytes
        license_data = license_data.tobytes()
    if isinstance(license_data, bytes):  # Convert binary to base64 string
        return base64.b64encode(license_data).decode("utf-8")
    return license_data  # If it's already a string, return as is

# Get all doctors working in a specific clinic
@router.get("/{clinic_id}/doctors", response_model=List[DoctorResponse])
def get_doctors_in_clinic(clinic_id: int, db: Session = Depends(get_db)):
    doctors = db.query(Doctor).filter(Doctor.clinic_id == clinic_id).all()
    
    if not doctors:
        raise HTTPException(status_code=404, detail="No doctors found for this clinic")

    # Convert license binary data to string
    for doctor in doctors:
        doctor.license = convert_license_to_string(doctor.license)

    return doctors
