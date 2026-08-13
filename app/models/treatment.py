from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float

from database import Base


class Treatment(Base):
    __tablename__ = "crop_treatments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    crop_id = Column(
        Integer,
        ForeignKey("crops.id"),
        nullable=False
    )

    product_name = Column(
        String(150),
        nullable=False
    )

    product_type = Column(
        String(100),
        nullable=False
    )

    quantity = Column(
        Float,
        nullable=False
    )

    applied_date = Column(
        Date,
        nullable=False
    )

    cost = Column(
        Float,
        nullable=False
    )

    remarks = Column(
        String(500),
        nullable=True
    )
