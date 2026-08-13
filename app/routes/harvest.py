from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Crop, Harvest
from schemas.harvest import HarvestCreate, HarvestResponse


router = APIRouter(
    prefix="/harvests",
    tags=["Harvests"]
)



# CREATE HARVEST


@router.post(
    "/",
    response_model=HarvestResponse
)
def create_harvest(
    harvest_data: HarvestCreate,
    db: Session = Depends(get_db)
):

    crop = db.query(Crop).filter(
        Crop.id == harvest_data.crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    harvest = Harvest(
        crop_id=harvest_data.crop_id,
        harvest_date=harvest_data.harvest_date,
        quantity=harvest_data.quantity,
        unit=harvest_data.unit,
        quality_grade=harvest_data.quality_grade,
        storage_location=harvest_data.storage_location
    )

    db.add(harvest)
    db.commit()
    db.refresh(harvest)

    return harvest



# GET ALL HARVESTS


@router.get(
    "/",
    response_model=list[HarvestResponse]
)
def get_harvests(
    db: Session = Depends(get_db)
):

    return db.query(Harvest).all()



# GET HARVEST BY ID


@router.get(
    "/{harvest_id}",
    response_model=HarvestResponse
)
def get_harvest(
    harvest_id: int,
    db: Session = Depends(get_db)
):

    harvest = db.query(Harvest).filter(
        Harvest.id == harvest_id
    ).first()

    if not harvest:
        raise HTTPException(
            status_code=404,
            detail="Harvest not found"
        )

    return harvest



# UPDATE HARVEST


@router.put(
    "/{harvest_id}",
    response_model=HarvestResponse
)
def update_harvest(
    harvest_id: int,
    harvest_data: HarvestCreate,
    db: Session = Depends(get_db)
):

    harvest = db.query(Harvest).filter(
        Harvest.id == harvest_id
    ).first()

    if not harvest:
        raise HTTPException(
            status_code=404,
            detail="Harvest not found"
        )

    crop = db.query(Crop).filter(
        Crop.id == harvest_data.crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    harvest.crop_id = harvest_data.crop_id
    harvest.harvest_date = harvest_data.harvest_date
    harvest.quantity = harvest_data.quantity
    harvest.unit = harvest_data.unit
    harvest.quality_grade = harvest_data.quality_grade
    harvest.storage_location = harvest_data.storage_location

    db.commit()
    db.refresh(harvest)

    return harvest



# DELETE HARVEST


@router.delete(
    "/{harvest_id}"
)
def delete_harvest(
    harvest_id: int,
    db: Session = Depends(get_db)
):

    harvest = db.query(Harvest).filter(
        Harvest.id == harvest_id
    ).first()

    if not harvest:
        raise HTTPException(
            status_code=404,
            detail="Harvest not found"
        )

    db.delete(harvest)
    db.commit()

    return {
        "message": "Harvest deleted successfully"
    }
