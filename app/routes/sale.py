from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Harvest, Sale
from schemas.sale import SaleCreate, SaleResponse


router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)


# ==========================
# CREATE SALE
# ==========================

@router.post(
    "/",
    response_model=SaleResponse
)
def create_sale(
    sale_data: SaleCreate,
    db: Session = Depends(get_db)
):

    harvest = db.query(Harvest).filter(
        Harvest.id == sale_data.harvest_id
    ).first()

    if not harvest:
        raise HTTPException(
            status_code=404,
            detail="Harvest not found"
        )

    if sale_data.quantity > harvest.quantity:
        raise HTTPException(
            status_code=400,
            detail="Sale quantity cannot exceed available harvest quantity"
        )

    total_amount = (
        sale_data.quantity * sale_data.price_per_unit
    )

    sale = Sale(
        harvest_id=sale_data.harvest_id,
        buyer_name=sale_data.buyer_name,
        quantity=sale_data.quantity,
        price_per_unit=sale_data.price_per_unit,
        total_amount=total_amount,
        sale_date=sale_data.sale_date,
        payment_status=sale_data.payment_status
    )

    db.add(sale)
    db.commit()
    db.refresh(sale)

    return sale


# ==========================
# GET ALL SALES
# ==========================

@router.get(
    "/",
    response_model=list[SaleResponse]
)
def get_sales(
    db: Session = Depends(get_db)
):

    return db.query(Sale).all()


# ==========================
# GET SALE BY ID
# ==========================

@router.get(
    "/{sale_id}",
    response_model=SaleResponse
)
def get_sale(
    sale_id: int,
    db: Session = Depends(get_db)
):

    sale = db.query(Sale).filter(
        Sale.id == sale_id
    ).first()

    if not sale:
        raise HTTPException(
            status_code=404,
            detail="Sale not found"
        )

    return sale


# ==========================
# UPDATE SALE
# ==========================

@router.put(
    "/{sale_id}",
    response_model=SaleResponse
)
def update_sale(
    sale_id: int,
    sale_data: SaleCreate,
    db: Session = Depends(get_db)
):

    sale = db.query(Sale).filter(
        Sale.id == sale_id
    ).first()

    if not sale:
        raise HTTPException(
            status_code=404,
            detail="Sale not found"
        )

    harvest = db.query(Harvest).filter(
        Harvest.id == sale_data.harvest_id
    ).first()

    if not harvest:
        raise HTTPException(
            status_code=404,
            detail="Harvest not found"
        )

    if sale_data.quantity > harvest.quantity:
        raise HTTPException(
            status_code=400,
            detail="Sale quantity cannot exceed available harvest quantity"
        )

    sale.harvest_id = sale_data.harvest_id
    sale.buyer_name = sale_data.buyer_name
    sale.quantity = sale_data.quantity
    sale.price_per_unit = sale_data.price_per_unit
    sale.total_amount = (
        sale_data.quantity * sale_data.price_per_unit
    )
    sale.sale_date = sale_data.sale_date
    sale.payment_status = sale_data.payment_status

    db.commit()
    db.refresh(sale)

    return sale


# ==========================
# DELETE SALE
# ==========================

@router.delete(
    "/{sale_id}"
)
def delete_sale(
    sale_id: int,
    db: Session = Depends(get_db)
):

    sale = db.query(Sale).filter(
        Sale.id == sale_id
    ).first()

    if not sale:
        raise HTTPException(
            status_code=404,
            detail="Sale not found"
        )

    db.delete(sale)
    db.commit()

    return {
        "message": "Sale deleted successfully"
    }
