from datetime import date

from pydantic import BaseModel, Field


class TreatmentCreate(BaseModel):

    crop_id: int

    product_name: str

    product_type: str

    quantity: float = Field(..., gt=0)

    applied_date: date

    cost: float = Field(..., ge=0)

    remarks: str | None = None


class TreatmentResponse(BaseModel):

    id: int

    crop_id: int

    product_name: str

    product_type: str

    quantity: float

    applied_date: date

    cost: float

    remarks: str | None

    class Config:
        from_attributes = True
