from pydantic import BaseModel
from typing import Optional

# class FirebaseOTPRequest(BaseModel):
#     firebase_token: str
#     name: str
#     age: int
#     email: str
#     address: Optional[str] = None
#     preferred_clinic: Optional[str] = None
#     location_access: bool

# from pydantic import BaseModel, EmailStr, Field
# from typing import Optional

# class OTPRequest(BaseModel):
#     phone_number: str = Field(..., min_length=10, max_length=20)

# class OTPVerifyRequest(BaseModel):
#     firebase_token: str
#     name: str
#     age: Optional[int] = Field(None, ge=0)  # `conint(ge=0)` replaced with `Field`
#     email: Optional[EmailStr]
#     address: Optional[str]
#     location_access: bool
#     preferred_clinic: Optional[str]

from uuid import UUID

class DoctorResponse(BaseModel):
    dr_id: str  # UUID stored as a string
    doc_name: str
    phone_number: int
    speciality: str
    year_of_experience: Optional[int]  # Optional for nullable fields
    estimated_patients: Optional[int]
    available_time: bool
    license:str   
    consultation_fee: Optional[float]
    clinic_id:int

    class Config:
        from_attributes = True  # For Pydantic V2 compatibility


class ClinicBase(BaseModel):
    clinic_name: str
    clinic_address: str
    clinic_area: str

class ClinicResponse(ClinicBase):
    clinic_id: int

    class Config:
        from_attributes = True  # For Pydantic V2 compatibility


