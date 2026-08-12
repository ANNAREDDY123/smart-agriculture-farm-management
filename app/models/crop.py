from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Crop(Base):

    __tablename__ = "crops"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    field_id = Column(
        Integer,
        ForeignKey("fields.id"),
        nullable=False,
        index=True
    )

    crop_name = Column(
        String(150),
        nullable=False,
        index=True
    )

    crop_type = Column(
        String(100),
        nullable=False
    )

    planting_date = Column(
        Date,
        nullable=False
    )

    expected_harvest_date = Column(
        Date,
        nullable=False
    )

    seed_quantity = Column(
        Float,
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="Planned"
    )

    field = relationship(
        "Field",
        back_populates="crops"
    )

    irrigation_records = relationship(
        "Irrigation",
        back_populates="crop",
        cascade="all, delete-orphan"
    )

    treatments = relationship(
        "Treatment",
        back_populates="crop",
        cascade="all, delete-orphan"
    )

    health_records = relationship(
        "CropHealth",
        back_populates="crop",
        cascade="all, delete-orphan"
    )

    harvests = relationship(
        "Harvest",
        back_populates="crop",
        cascade="all, delete-orphan"
    )
