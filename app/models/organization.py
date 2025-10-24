from typing import TYPE_CHECKING

from sqlalchemy import String, Table, Column, MetaData, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from models.activities import Activity

if TYPE_CHECKING:
    from app.models.phone_number import PhoneNumber
    from app.models.building import Building


organization_activities = Table(
    "organization_activities",
    Base.metadata,
    Column(
        "organization_id",
        Integer,
        ForeignKey(
            "organizations.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    ),
    Column(
        "activity_id",
        Integer,
        ForeignKey(
            "activities.id",
            ondelete="CASCADE",
        ),
        primary_key=True,
    ),
)


class Organization(Base):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    phone_number: Mapped[list[PhoneNumber]] = relationship(
        "PhoneNumber",
        backref="organization",
        cascade="all, delete-orphan",
    )

    building: Mapped[Building] = relationship(
        "Building",
        backref="organization",
        cascade="None",
    )

    activity: Mapped[list[Activity]] = relationship(
        "Activity",
        back_populates="organization",
        secondary=organization_activities,
    )
