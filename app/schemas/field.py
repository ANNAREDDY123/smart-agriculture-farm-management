from pydantic import BaseModel, Field


class FieldCreate(BaseModel):
    farm_id: int
    field_name: str = Field(..., min_length=2, max_length=100)
    area: float = Field(..., gt=0)
    soil_type: str = Field(..., min_length=2, max_length=100)
    irrigation_type: str = Field(..., min_length=2, max_length=100)
    status: str = "Active"


class FieldResponse(BaseModel):
    id: int
    farm_id: int
    field_name: str
    area: float
    soil_type: str
    irrigation_type: str
    status: str

    class Config:
        from_attributes = True
