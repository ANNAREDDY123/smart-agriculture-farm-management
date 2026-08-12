from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship

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
        nullable=False,
        index=True
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

    crop = relationship(
        "Crop",
        back_populates="treatments"
    )
