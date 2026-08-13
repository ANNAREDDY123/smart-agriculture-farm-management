from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Crop, Treatment
from schemas.treatment import TreatmentCreate, TreatmentResponse


router = APIRouter(
    prefix="/treatments",
    tags=["Treatments"]
)


@router.post(
    "/",
    response_model=TreatmentResponse
)
def create_treatment(
    treatment_data: TreatmentCreate,
    db: Session = Depends(get_db)
):

    crop = db.query(Crop).filter(
        Crop.id == treatment_data.crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    treatment = Treatment(
        crop_id=treatment_data.crop_id,
        treatment_type=treatment_data.treatment_type,
        treatment_date=treatment_data.treatment_date,
        description=treatment_data.description,
        status=treatment_data.status
    )

    db.add(treatment)
    db.commit()
    db.refresh(treatment)

    return treatment


@router.get(
    "/",
    response_model=list[TreatmentResponse]
)
def get_treatments(
    db: Session = Depends(get_db)
):

    return db.query(Treatment).all()


@router.get(
    "/{treatment_id}",
    response_model=TreatmentResponse
)
def get_treatment(
    treatment_id: int,
    db: Session = Depends(get_db)
):

    treatment = db.query(Treatment).filter(
        Treatment.id == treatment_id
    ).first()

    if not treatment:
        raise HTTPException(
            status_code=404,
            detail="Treatment not found"
        )

    return treatment


@router.put(
    "/{treatment_id}",
    response_model=TreatmentResponse
)
def update_treatment(
    treatment_id: int,
    treatment_data: TreatmentCreate,
    db: Session = Depends(get_db)
):

    treatment = db.query(Treatment).filter(
        Treatment.id == treatment_id
    ).first()

    if not treatment:
        raise HTTPException(
            status_code=404,
            detail="Treatment not found"
        )

    crop = db.query(Crop).filter(
        Crop.id == treatment_data.crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    treatment.crop_id = treatment_data.crop_id
    treatment.treatment_type = treatment_data.treatment_type
    treatment.treatment_date = treatment_data.treatment_date
    treatment.description = treatment_data.description
    treatment.status = treatment_data.status

    db.commit()
    db.refresh(treatment)

    return treatment


@router.delete(
    "/{treatment_id}"
)
def delete_treatment(
    treatment_id: int,
    db: Session = Depends(get_db)
):

    treatment = db.query(Treatment).filter(
        Treatment.id == treatment_id
    ).first()

    if not treatment:
        raise HTTPException(
            status_code=404,
            detail="Treatment not found"
        )

    db.delete(treatment)
    db.commit()

    return {
        "message": "Treatment deleted successfully"
    }
