from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Farm, Field
from schemas.field import FieldCreate, FieldResponse

router = APIRouter(
    prefix="/farms",
    tags=["Fields"]
)


@router.post("/{farm_id}/fields", response_model=FieldResponse)
def create_field(
    farm_id: int,
    field_data: FieldCreate,
    db: Session = Depends(get_db)
):
    # Check farm exists
    farm = db.query(Farm).filter(Farm.id == farm_id).first()

    if not farm:
        raise HTTPException(
            status_code=404,
            detail="Farm not found"
        )

    # Check farm is active
    if farm.status != "Active":
        raise HTTPException(
            status_code=400,
            detail="Cannot add field to an inactive farm"
        )

    # Check field name is unique within the farm
    existing_field = db.query(Field).filter(
        Field.farm_id == farm_id,
        Field.field_name == field_data.field_name
    ).first()

    if existing_field:
        raise HTTPException(
            status_code=400,
            detail="Field name already exists in this farm"
        )

    # Calculate already used area
    used_area = db.query(Field).filter(
        Field.farm_id == farm_id
    ).with_entities(
        Field.area
    ).all()

    total_used_area = sum(field.area for field in used_area)

    # Check available area
    if total_used_area + field_data.area > farm.total_area:
        raise HTTPException(
            status_code=400,
            detail="Field area exceeds the farm's available area"
        )

    # Create field
    field = Field(
        farm_id=farm_id,
        field_name=field_data.field_name,
        area=field_data.area,
        soil_type=field_data.soil_type,
        irrigation_type=field_data.irrigation_type,
        status=field_data.status
    )

    db.add(field)
    db.commit()
    db.refresh(field)

    return field


@router.get("/{farm_id}/fields", response_model=list[FieldResponse])
def get_fields(
    farm_id: int,
    db: Session = Depends(get_db)
):
    # Check farm exists
    farm = db.query(Farm).filter(Farm.id == farm_id).first()

    if not farm:
        raise HTTPException(
            status_code=404,
            detail="Farm not found"
        )

    return db.query(Field).filter(
        Field.farm_id == farm_id
    ).all()
