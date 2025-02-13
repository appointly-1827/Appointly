# from sqlalchemy import UUID, create_engine
# from sqlalchemy.orm import sessionmaker
# import psycopg2
# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session

# from models.doctor_model import Doctor
# from schemas import DoctorResponse
# from typing import List, Optional
from fastapi import FastAPI
from database import engine, Base
from routes.doctor_routes import router as doctor_router
from routes.clinic_routes import router as clinic_router
# Initialize FastAPI app
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)
app.include_router(doctor_router)
app.include_router(clinic_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Clinic Appointment API"}

# import base64

# def convert_license_to_string(license_data):
#     if isinstance(license_data, memoryview):  # If data is in memoryview format, convert to bytes
#         license_data = license_data.tobytes()
#     if isinstance(license_data, bytes):  # Convert binary to a base64 string
#         return base64.b64encode(license_data).decode("utf-8")
#     return license_data  # If it's already a string, return as is

# @app.get("/doctors", response_model=List[DoctorResponse])
# def get_doctors(
#     speciality: Optional[str] = None,
#     location: Optional[str] = None,
#     search: Optional[str] = None,
#     limit: int = 10,
#     offset: int = 0,
#     db: Session = Depends(get_db),
# ):
#     query = db.query(Doctor)

#     if speciality:
#         query = query.filter(Doctor.speciality.ilike(f"%{speciality}%"))
#     if search:
#         query = query.filter(Doctor.doc_name.ilike(f"%{search}%"))
#     if location:
#         query = query.filter(Doctor.clinic_id == location)

#     doctors = query.offset(offset).limit(limit).all()

#     # Convert binary license data to a valid string
#     for doctor in doctors:
#         doctor.license = convert_license_to_string(doctor.license)

#     return doctors


# @app.get("/doctors/{doctor_id}", response_model=DoctorResponse)
# def get_doctor_details(doctor_id: str, db: Session = Depends(get_db)):
#     # Ensure that the doctor_id is properly matched as a string
#     doctor = db.query(Doctor).filter(Doctor.dr_id == doctor_id).first()
    
#     if not doctor:
#         raise HTTPException(status_code=404, detail="Doctor not found")
    
#     return doctor

# @app.post("/adddoc")
# def create_doctor(doctor: DoctorResponse, db: Session = Depends(get_db)):
#     # Create the doctor object
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
    
#     # Add doctor to the database
#     db.add(db_doctor)
#     db.commit()
#     db.refresh(db_doctor)
    
#     return {"message": "Doctor created successfully", "doctor_id": db_doctor.dr_id}

# @app.get("/")
# def root():
#     return {"message": "Welcome to the Clinic Appointment API"}
