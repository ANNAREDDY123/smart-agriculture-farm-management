from datetime import date

from pydantic import BaseModel, Field


class CropCreate(BaseModel):
    field_id: int
    crop_name: str = Field(..., min_length=2, max_length=100)
    crop_type: str = Field(..., min_length=2, max_length=100)
    planting_date: date
    expected_harvest_date: date
    seed_quantity: float = Field(..., gt=0)
    status: str = "Planned"


class CropUpdate(BaseModel):
    crop_name: str | None = Field(None, min_length=2, max_length=100)
    crop_type: str | None = Field(None, min_length=2, max_length=100)
    planting_date: date | None = None
    expected_harvest_date: date | None = None
    seed_quantity: float | None = Field(None, gt=0)
    status: str | None = None


class CropResponse(BaseModel):
    id: int
    field_id: int
    crop_name: str
    crop_type: str
    planting_date: date
    expected_harvest_date: date
    seed_quantity: float
    status: str

    class Config:
        from_attributes = True
