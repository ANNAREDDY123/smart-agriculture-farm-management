from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Field(Base):

    __tablename__ = "fields"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    farm_id = Column(
        Integer,
        ForeignKey("farms.id"),
        nullable=False,
        index=True
    )

    field_name = Column(
        String(150),
        nullable=False,
        index=True
    )

    area = Column(
        Float,
        nullable=False
    )

    soil_type = Column(
        String(100),
        nullable=False
    )

    irrigation_type = Column(
        String(100),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="Active"
    )

    farm = relationship(
        "Farm",
        back_populates="fields"
    )

    crops = relationship(
        "Crop",
        back_populates="field",
        cascade="all, delete-orphan"
    )
