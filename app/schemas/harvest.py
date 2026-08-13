from datetime import date

from pydantic import BaseModel, Field


class HarvestCreate(BaseModel):

    crop_id: int

    harvest_date: date

    quantity: float = Field(..., gt=0)

    unit: str

    quality_grade: str

    storage_location: str


class HarvestResponse(BaseModel):

    id: int
    crop_id: int
    harvest_date: date
    quantity: float
    unit: str
    quality_grade: str
    storage_location: str

    class Config:
        from_attributes = True
