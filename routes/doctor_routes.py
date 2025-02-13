from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
import base64

from database import get_db
from models.doctor_model import Doctor
from models.clinic_model import Clinic
from schemas import DoctorResponse , DoctorBase

# Create a router for doctors
router = APIRouter(prefix="/doctors", tags=["Doctors"])

# Function to convert binary license data to string
def convert_license_to_string(license_data):
    if isinstance(license_data, memoryview):
        license_data = license_data.tobytes()
    if isinstance(license_data, bytes):
        return base64.b64encode(license_data).decode("utf-8")
    return license_data

# Get list of doctors with optional filters
@router.get("/", response_model=List[DoctorResponse])
def get_doctors(
    speciality: Optional[str] = None,
    location: Optional[str] = None,
    search: Optional[str] = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
):
    query = db.query(Doctor)

    if speciality:
        query = query.filter(Doctor.speciality.ilike(f"%{speciality}%"))
    if search:
        query = query.filter(Doctor.doc_name.ilike(f"%{search}%"))
    if location:
        query = query.filter(Doctor.clinic_id == location)

    doctors = query.offset(offset).limit(limit).all()

    # Convert binary license data to a valid string
    for doctor in doctors:
        doctor.license = convert_license_to_string(doctor.license)

    return doctors

# Get details of a specific doctor
@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor_details(doctor_id: str, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.dr_id == doctor_id).first()

    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")

    return doctor

# Add a new doctor
# @router.post("/add")
# def create_doctor(doctor: DoctorResponse, db: Session = Depends(get_db)):
#     db_doctor = Doctor(
#         doc_name=doctor.doc_name,
#         phone_number=doctor.phone_number,
#         speciality=doctor.speciality,
#         year_of_experience=doctor.year_of_experience,
#         estimated_patients=doctor.estimated_patients,
#         available_time=doctor.available_time,
#         license=doctor.license,
#         consultation_fee=doctor.consultation_fee,
#         clinic_id=doctor.clinic_id,
#     )

#     db.add(db_doctor)
#     db.commit()
#     db.refresh(db_doctor)

#     return {"message": "Doctor created successfully", "doctor_id": db_doctor.dr_id}


@router.post("/add", response_model=DoctorResponse)
def create_doctor(doctor: DoctorBase, db: Session = Depends(get_db)):
    # If clinic_id is not provided, use a default clinic (e.g., ID 1)
    if not doctor.clinic_id:
        default_clinic = db.query(Clinic).filter(Clinic.clinic_id == 1).first()
        if not default_clinic:
            raise HTTPException(status_code=400, detail="Default clinic not found")
        doctor.clinic_id = default_clinic.clinic_id  # Assign default clinic
    
    # Create and save the doctor record
    db_doctor = Doctor(
        doc_name=doctor.doc_name,
        phone_number=doctor.phone_number,
        speciality=doctor.speciality,
        year_of_experience=doctor.year_of_experience,
        estimated_patients=doctor.estimated_patients,
        available_time=doctor.available_time,
        license=doctor.license,
        consultation_fee=doctor.consultation_fee,
        clinic_id=doctor.clinic_id
    )
    
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return db_doctor
