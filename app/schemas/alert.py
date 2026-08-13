from datetime import datetime

from pydantic import BaseModel, Field


class AlertCreate(BaseModel):

    crop_id: int

    message: str = Field(
        ...,
        min_length=2,
        max_length=500
    )

    alert_type: str = Field(
        default="Crop Health",
        max_length=100
    )

    is_read: bool = False


class AlertResponse(BaseModel):

    id: int
    crop_id: int
    message: str
    alert_type: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True
