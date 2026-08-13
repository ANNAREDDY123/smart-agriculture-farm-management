from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Crop, Field
from schemas.crop import (
    CropCreate,
    CropUpdate,
    CropResponse
)

router = APIRouter(
    prefix="/crops",
    tags=["Crops"]
)



# CREATE CROP

@router.post(
    "/",
    response_model=CropResponse
)
def create_crop(
    crop_data: CropCreate,
    db: Session = Depends(get_db)
):

    # Check field exists
    field = db.query(Field).filter(
        Field.id == crop_data.field_id
    ).first()

    if not field:
        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )

    # Inactive fields cannot be used
    if field.status != "Active":
        raise HTTPException(
            status_code=400,
            detail="Inactive fields cannot be used for new crop cultivation"
        )

    # Validate dates
    if crop_data.planting_date > crop_data.expected_harvest_date:
        raise HTTPException(
            status_code=400,
            detail="Planting date cannot be after expected harvest date"
        )

    # Check for overlapping active crops
    active_statuses = [
        "Planned",
        "Growing",
        "Ready for Harvest"
    ]

    existing_crops = db.query(Crop).filter(
        Crop.field_id == crop_data.field_id,
        Crop.status.in_(active_statuses)
    ).all()

    for existing_crop in existing_crops:

        if (
            crop_data.planting_date
            <= existing_crop.expected_harvest_date
            and
            crop_data.expected_harvest_date
            >= existing_crop.planting_date
        ):
            raise HTTPException(
                status_code=400,
                detail="Crop dates overlap with an existing active crop"
            )

    # Create crop
    crop = Crop(
        field_id=crop_data.field_id,
        crop_name=crop_data.crop_name,
        crop_type=crop_data.crop_type,
        planting_date=crop_data.planting_date,
        expected_harvest_date=crop_data.expected_harvest_date,
        seed_quantity=crop_data.seed_quantity,
        status=crop_data.status
    )

    db.add(crop)
    db.commit()
    db.refresh(crop)

    return crop



# GET ALL CROPS


@router.get(
    "/",
    response_model=list[CropResponse]
)
def get_crops(
    db: Session = Depends(get_db)
):

    return db.query(Crop).all()


# GET CROP BY ID


@router.get(
    "/{crop_id}",
    response_model=CropResponse
)
def get_crop(
    crop_id: int,
    db: Session = Depends(get_db)
):

    crop = db.query(Crop).filter(
        Crop.id == crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    return crop


# UPDATE CROP


@router.put(
    "/{crop_id}",
    response_model=CropResponse
)
def update_crop(
    crop_id: int,
    crop_data: CropUpdate,
    db: Session = Depends(get_db)
):

    crop = db.query(Crop).filter(
        Crop.id == crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    # Harvested crops cannot be modified
    if crop.status == "Harvested":
        raise HTTPException(
            status_code=400,
            detail="Harvested crops cannot be modified"
        )

    update_data = crop_data.model_dump(
        exclude_unset=True
    )

    # Validate updated dates
    planting_date = update_data.get(
        "planting_date",
        crop.planting_date
    )

    harvest_date = update_data.get(
        "expected_harvest_date",
        crop.expected_harvest_date
    )

    if planting_date > harvest_date:
        raise HTTPException(
            status_code=400,
            detail="Planting date cannot be after expected harvest date"
        )

    # If dates are being changed, check overlap
    if (
        "planting_date" in update_data
        or "expected_harvest_date" in update_data
    ):

        active_statuses = [
            "Planned",
            "Growing",
            "Ready for Harvest"
        ]

        existing_crops = db.query(Crop).filter(
            Crop.field_id == crop.field_id,
            Crop.id != crop.id,
            Crop.status.in_(active_statuses)
        ).all()

        for existing_crop in existing_crops:

            if (
                planting_date
                <= existing_crop.expected_harvest_date
                and
                harvest_date
                >= existing_crop.planting_date
            ):
                raise HTTPException(
                    status_code=400,
                    detail="Crop dates overlap with an existing active crop"
                )

    for key, value in update_data.items():
        setattr(crop, key, value)

    db.commit()
    db.refresh(crop)

    return crop
