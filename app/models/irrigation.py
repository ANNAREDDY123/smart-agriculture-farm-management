from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Irrigation(Base):

    __tablename__ = "irrigation"

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

    crop_id = Column(
        Integer,
        ForeignKey("crops.id"),
        nullable=False,
        index=True
    )

    irrigation_date = Column(
        DateTime,
        nullable=False
    )

    water_quantity = Column(
        Float,
        nullable=False
    )

    duration_minutes = Column(
        Integer,
        nullable=False
    )

    irrigation_status = Column(
        String(50),
        nullable=False,
        default="Completed"
    )

    remarks = Column(
        String(500),
        nullable=True
    )

    crop = relationship(
        "Crop",
        back_populates="irrigation_records"
    )

    field = relationship(
        "Field"
    )
