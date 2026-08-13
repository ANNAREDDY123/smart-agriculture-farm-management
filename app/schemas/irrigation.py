from datetime import date

from pydantic import BaseModel, Field


class IrrigationCreate(BaseModel):
    field_id: int
    irrigation_date: date
    water_quantity: float = Field(..., gt=0)
    duration_minutes: int = Field(..., gt=0)
    irrigation_status: str = "Completed"
    remarks: str | None = None


class IrrigationResponse(BaseModel):
    id: int
    field_id: int
    crop_id: int
    irrigation_date: date
    water_quantity: float
    duration_minutes: int
    irrigation_status: str
    remarks: str | None

    class Config:
        from_attributes = True
