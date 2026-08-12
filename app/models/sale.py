from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Sale(Base):

    __tablename__ = "sales"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    harvest_id = Column(
        Integer,
        ForeignKey("harvests.id"),
        nullable=False,
        index=True
    )

    buyer_name = Column(
        String(150),
        nullable=False,
        index=True
    )

    quantity = Column(
        Float,
        nullable=False
    )

    price_per_unit = Column(
        Float,
        nullable=False
    )

    total_amount = Column(
        Float,
        nullable=False
    )

    sale_date = Column(
        Date,
        nullable=False
    )

    payment_status = Column(
        String(50),
        nullable=False,
        default="Pending"
    )

    harvest = relationship(
        "Harvest",
        back_populates="sales"
    )
