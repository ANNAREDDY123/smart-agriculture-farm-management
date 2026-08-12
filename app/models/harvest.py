from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Harvest(Base):

    __tablename__ = "harvests"

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

    harvest_date = Column(
        Date,
        nullable=False
    )

    quantity = Column(
        Float,
        nullable=False
    )

    unit = Column(
        String(50),
        nullable=False
    )

    quality_grade = Column(
        String(50),
        nullable=False
    )

    storage_location = Column(
        String(200),
        nullable=False
    )

    crop = relationship(
        "Crop",
        back_populates="harvests"
    )

    sales = relationship(
        "Sale",
        back_populates="harvest",
        cascade="all, delete-orphan"
    )
