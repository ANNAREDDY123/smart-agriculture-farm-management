from datetime import date

from pydantic import BaseModel


class TreatmentCreate(BaseModel):
    crop_id: int
    treatment_type: str
    treatment_date: date
    description: str | None = None
    status: str = "Completed"


class TreatmentResponse(BaseModel):
    id: int
    crop_id: int
    treatment_type: str
    treatment_date: date
    description: str | None
    status: str

    class Config:
        from_attributes = True
