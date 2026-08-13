from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class CropHealth(Base):

    __tablename__ = "crop_health"

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

    inspection_date = Column(
        Date,
        nullable=False
    )

    health_status = Column(
        String(50),
        nullable=False
    )

    disease_name = Column(
        String(150),
        nullable=True
    )

    severity = Column(
        String(50),
        nullable=True
    )

    remarks = Column(
        String(500),
        nullable=True
    )

    crop = relationship(
        "Crop",
        back_populates="health_records"
    )
