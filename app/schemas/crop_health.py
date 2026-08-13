from datetime import date

from pydantic import BaseModel, Field


class CropHealthCreate(BaseModel):

    crop_id: int

    inspection_date: date

    health_status: str = Field(
        ...,
        min_length=2,
        max_length=50
    )

    disease_name: str | None = Field(
        default=None,
        max_length=150
    )

    severity: str | None = Field(
        default=None,
        max_length=50
    )

    remarks: str | None = Field(
        default=None,
        max_length=500
    )


class CropHealthResponse(BaseModel):

    id: int
    crop_id: int
    inspection_date: date
    health_status: str
    disease_name: str | None
    severity: str | None
    remarks: str | None

    class Config:
        from_attributes = True
