from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Farm
from schemas.farm import FarmCreate, FarmUpdate, FarmResponse

router = APIRouter(
    prefix="/farms",
    tags=["Farms"]
)


@router.post("/", response_model=FarmResponse)
def create_farm(
    farm_data: FarmCreate,
    db: Session = Depends(get_db)
):
    existing_farm = db.query(Farm).filter(
        Farm.farm_name == farm_data.farm_name
    ).first()

    if existing_farm:
        raise HTTPException(
            status_code=400,
            detail="Farm name already exists"
        )

    farm = Farm(**farm_data.model_dump())

    db.add(farm)
    db.commit()
    db.refresh(farm)

    return farm


@router.get("/", response_model=list[FarmResponse])
def get_farms(
    db: Session = Depends(get_db)
):
    return db.query(Farm).all()


@router.get("/{farm_id}", response_model=FarmResponse)
def get_farm(
    farm_id: int,
    db: Session = Depends(get_db)
):
    farm = db.query(Farm).filter(Farm.id == farm_id).first()

    if not farm:
        raise HTTPException(
            status_code=404,
            detail="Farm not found"
        )

    return farm


@router.put("/{farm_id}", response_model=FarmResponse)
def update_farm(
    farm_id: int,
    farm_data: FarmUpdate,
    db: Session = Depends(get_db)
):
    farm = db.query(Farm).filter(Farm.id == farm_id).first()

    if not farm:
        raise HTTPException(
            status_code=404,
            detail="Farm not found"
        )

    update_data = farm_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(farm, key, value)

    db.commit()
    db.refresh(farm)

    return farm
