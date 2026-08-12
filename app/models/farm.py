from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Farm(Base):

    __tablename__ = "farms"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    farm_name = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    location = Column(
        String(200),
        nullable=False,
        index=True
    )

    total_area = Column(
        Float,
        nullable=False
    )

    owner_name = Column(
        String(150),
        nullable=False
    )

    status = Column(
        String(50),
        nullable=False,
        default="Active"
    )

    fields = relationship(
        "Field",
        back_populates="farm",
        cascade="all, delete-orphan"
    )
