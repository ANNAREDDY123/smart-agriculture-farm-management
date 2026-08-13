from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Crop, CropHealth
from schemas.crop_health import (
    CropHealthCreate,
    CropHealthResponse
)


router = APIRouter(
    prefix="/crop-health",
    tags=["Crop Health"]
)



# CREATE CROP HEALTH RECORD


@router.post(
    "/",
    response_model=CropHealthResponse
)
def create_crop_health(
    health_data: CropHealthCreate,
    db: Session = Depends(get_db)
):

    crop = db.query(Crop).filter(
        Crop.id == health_data.crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    health = CropHealth(
        crop_id=health_data.crop_id,
        inspection_date=health_data.inspection_date,
        health_status=health_data.health_status,
        disease_name=health_data.disease_name,
        severity=health_data.severity,
        remarks=health_data.remarks
    )

    db.add(health)
    db.commit()
    db.refresh(health)

    return health



# GET ALL HEALTH RECORDS


@router.get(
    "/",
    response_model=list[CropHealthResponse]
)
def get_crop_health_records(
    db: Session = Depends(get_db)
):

    return db.query(CropHealth).all()



# GET HEALTH RECORD BY ID


@router.get(
    "/{health_id}",
    response_model=CropHealthResponse
)
def get_crop_health(
    health_id: int,
    db: Session = Depends(get_db)
):

    health = db.query(CropHealth).filter(
        CropHealth.id == health_id
    ).first()

    if not health:
        raise HTTPException(
            status_code=404,
            detail="Crop health record not found"
        )

    return health



# UPDATE HEALTH RECORD


@router.put(
    "/{health_id}",
    response_model=CropHealthResponse
)
def update_crop_health(
    health_id: int,
    health_data: CropHealthCreate,
    db: Session = Depends(get_db)
):

    health = db.query(CropHealth).filter(
        CropHealth.id == health_id
    ).first()

    if not health:
        raise HTTPException(
            status_code=404,
            detail="Crop health record not found"
        )

    crop = db.query(Crop).filter(
        Crop.id == health_data.crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    health.crop_id = health_data.crop_id
    health.inspection_date = health_data.inspection_date
    health.health_status = health_data.health_status
    health.disease_name = health_data.disease_name
    health.severity = health_data.severity
    health.remarks = health_data.remarks

    db.commit()
    db.refresh(health)

    return health



# DELETE HEALTH RECORD


@router.delete(
    "/{health_id}"
)
def delete_crop_health(
    health_id: int,
    db: Session = Depends(get_db)
):

    health = db.query(CropHealth).filter(
        CropHealth.id == health_id
    ).first()

    if not health:
        raise HTTPException(
            status_code=404,
            detail="Crop health record not found"
        )

    db.delete(health)
    db.commit()

    return {
        "message": "Crop health record deleted successfully"
    }
