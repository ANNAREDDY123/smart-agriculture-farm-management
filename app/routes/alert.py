from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Alert, Crop
from schemas.alert import AlertCreate, AlertResponse


router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)



# CREATE ALERT


@router.post(
    "/",
    response_model=AlertResponse
)
def create_alert(
    alert_data: AlertCreate,
    db: Session = Depends(get_db)
):

    crop = db.query(Crop).filter(
        Crop.id == alert_data.crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    alert = Alert(
        crop_id=alert_data.crop_id,
        message=alert_data.message,
        alert_type=alert_data.alert_type,
        is_read=alert_data.is_read,
        created_at=datetime.now()
    )

    db.add(alert)
    db.commit()
    db.refresh(alert)

    return alert



# GET ALL ALERTS


@router.get(
    "/",
    response_model=list[AlertResponse]
)
def get_alerts(
    db: Session = Depends(get_db)
):

    return db.query(Alert).order_by(
        Alert.created_at.desc()
    ).all()



# GET ALERT BY ID


@router.get(
    "/{alert_id}",
    response_model=AlertResponse
)
def get_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):

    alert = db.query(Alert).filter(
        Alert.id == alert_id
    ).first()

    if not alert:
        raise HTTPException(
            status_code=404,
            detail="Alert not found"
        )

    return alert



# UPDATE ALERT


@router.put(
    "/{alert_id}",
    response_model=AlertResponse
)
def update_alert(
    alert_id: int,
    alert_data: AlertCreate,
    db: Session = Depends(get_db)
):

    alert = db.query(Alert).filter(
        Alert.id == alert_id
    ).first()

    if not alert:
        raise HTTPException(
            status_code=404,
            detail="Alert not found"
        )

    crop = db.query(Crop).filter(
        Crop.id == alert_data.crop_id
    ).first()

    if not crop:
        raise HTTPException(
            status_code=404,
            detail="Crop not found"
        )

    alert.crop_id = alert_data.crop_id
    alert.message = alert_data.message
    alert.alert_type = alert_data.alert_type
    alert.is_read = alert_data.is_read

    db.commit()
    db.refresh(alert)

    return alert



# DELETE ALERT


@router.delete(
    "/{alert_id}"
)
def delete_alert(
    alert_id: int,
    db: Session = Depends(get_db)
):

    alert = db.query(Alert).filter(
        Alert.id == alert_id
    ).first()

    if not alert:
        raise HTTPException(
            status_code=404,
            detail="Alert not found"
        )

    db.delete(alert)
    db.commit()

    return {
        "message": "Alert deleted successfully"
    }
