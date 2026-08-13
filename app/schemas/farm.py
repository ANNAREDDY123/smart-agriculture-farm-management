from pydantic import BaseModel, Field


class FarmCreate(BaseModel):
    farm_name: str = Field(..., min_length=2, max_length=100)
    location: str = Field(..., min_length=2, max_length=200)
    total_area: float = Field(..., gt=0)
    owner_name: str = Field(..., min_length=2, max_length=100)
    status: str = "Active"


class FarmUpdate(BaseModel):
    farm_name: str | None = Field(None, min_length=2, max_length=100)
    location: str | None = Field(None, min_length=2, max_length=200)
    total_area: float | None = Field(None, gt=0)
    owner_name: str | None = Field(None, min_length=2, max_length=100)
    status: str | None = None


class FarmResponse(BaseModel):
    id: int
    farm_name: str
    location: str
    total_area: float
    owner_name: str
    status: str

    class Config:
        from_attributes = True
