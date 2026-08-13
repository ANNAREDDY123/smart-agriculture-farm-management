from sqlalchemy import Column, Integer, String, Date, ForeignKey, Text

from database import Base


class Treatment(Base):
    __tablename__ = "treatments"

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

    treatment_type = Column(
        String(100),
        nullable=False
    )

    treatment_date = Column(
        Date,
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    status = Column(
        String(50),
        nullable=False,
        default="Completed"
    )
