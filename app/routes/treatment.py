from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Crop, Treatment
from schemas.treatment import TreatmentCreate, TreatmentResponse


router = APIRouter(
    prefix="/treatments",
    tags=["Treatments"]
)


# CREATE TREATMENT


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
        product_name=treatment_data.product_name,
        product_type=treatment_data.product_type,
        quantity=treatment_data.quantity,
        applied_date=treatment_data.applied_date,
        cost=treatment_data.cost,
        remarks=treatment_data.remarks
    )

    db.add(treatment)
    db.commit()
    db.refresh(treatment)

    return treatment



# GET ALL TREATMENTS


@router.get(
    "/",
    response_model=list[TreatmentResponse]
)
def get_treatments(
    db: Session = Depends(get_db)
):

    return db.query(Treatment).all()



# GET TREATMENT BY ID


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


# UPDATE TREATMENT


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
    treatment.product_name = treatment_data.product_name
    treatment.product_type = treatment_data.product_type
    treatment.quantity = treatment_data.quantity
    treatment.applied_date = treatment_data.applied_date
    treatment.cost = treatment_data.cost
    treatment.remarks = treatment_data.remarks

    db.commit()
    db.refresh(treatment)

    return treatment



# DELETE TREATMENT


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
