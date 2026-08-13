from datetime import date
from typing import Literal

from pydantic import BaseModel, Field


class SaleCreate(BaseModel):

    harvest_id: int

    buyer_name: str = Field(..., min_length=2, max_length=150)

    quantity: float = Field(..., gt=0)

    price_per_unit: float = Field(..., gt=0)

    sale_date: date

    payment_status: Literal["Pending", "Paid", "Partial"] = "Pending"


class SaleResponse(BaseModel):

    id: int
    harvest_id: int
    buyer_name: str
    quantity: float
    price_per_unit: float
    total_amount: float
    sale_date: date
    payment_status: str

    class Config:
        from_attributes = True
