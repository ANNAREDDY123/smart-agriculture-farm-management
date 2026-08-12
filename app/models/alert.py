from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Alert(Base):

    __tablename__ = "alerts"

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

    message = Column(
        String(500),
        nullable=False
    )

    alert_type = Column(
        String(100),
        nullable=False,
        default="Crop Health"
    )

    is_read = Column(
        String(20),
        nullable=False,
        default="False"
    )

    created_at = Column(
        DateTime,
        nullable=False
    )

    crop = relationship("Crop")
