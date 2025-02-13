from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class DoctorResponse(BaseModel):
    dr_id: str  # UUID stored as a string
    doc_name: str
    phone_number: int
    speciality: str
    year_of_experience: Optional[int]  # Optional for nullable fields
    estimated_patients: Optional[int]
    available_time: bool
    license: Optional[str] = None   
    consultation_fee: Optional[float]
    clinic_id:int

    class Config:
        from_attributes = True  # For Pydantic V2 compatibility


class DoctorBase(BaseModel):
    doc_name: str
    phone_number: int
    speciality: str
    year_of_experience: Optional[int] = None
    estimated_patients: Optional[int] = None
    available_time: Optional[bool] = True
    license: Optional[str] = None
    consultation_fee: Optional[float] = None
    clinic_id: Optional[int] = None



class ClinicCreate(BaseModel):
    clinic_name: str
    clinic_address: str
    clinic_area: str

class ClinicResponse(ClinicCreate):
    clinic_id: int

    class Config:
        from_attributes = True  # For Pydantic V2 compatibility


