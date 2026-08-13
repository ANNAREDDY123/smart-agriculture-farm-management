from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Field, Crop, Irrigation
from schemas.irrigation import IrrigationCreate, IrrigationResponse

router = APIRouter(tags=["Irrigation"])


@router.post(
    "/irrigation",
    response_model=IrrigationResponse
)
def create_irrigation(
    irrigation_data: IrrigationCreate,
    db: Session = Depends(get_db)
):

    field = db.query(Field).filter(
        Field.id == irrigation_data.field_id
    ).first()

    if not field:
        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )

    active_statuses = [
        "Planned",
        "Growing",
        "Ready for Harvest"
    ]

    active_crop = db.query(Crop).filter(
        Crop.field_id == irrigation_data.field_id,
        Crop.status.in_(active_statuses)
    ).first()

    if not active_crop:
        raise HTTPException(
            status_code=400,
            detail="Irrigation can be recorded only for fields with active crops"
        )

    irrigation = Irrigation(
        field_id=irrigation_data.field_id,
        crop_id=active_crop.id,
        irrigation_date=irrigation_data.irrigation_date,
        water_quantity=irrigation_data.water_quantity,
        duration_minutes=irrigation_data.duration_minutes,
        irrigation_status=irrigation_data.irrigation_status,
        remarks=irrigation_data.remarks
    )

    db.add(irrigation)
    db.commit()
    db.refresh(irrigation)

    return irrigation


@router.get(
    "/irrigation",
    response_model=list[IrrigationResponse]
)
def get_irrigation(
    db: Session = Depends(get_db)
):
    return db.query(Irrigation).all()


@router.get(
    "/fields/{field_id}/irrigation",
    response_model=list[IrrigationResponse]
)
def get_field_irrigation(
    field_id: int,
    db: Session = Depends(get_db)
):

    field = db.query(Field).filter(
        Field.id == field_id
    ).first()

    if not field:
        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )

    return db.query(Irrigation).filter(
        Irrigation.field_id == field_id
    ).all()
