from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.activities import Activity
    from app.models.building import Building
    from app.models.phone_number import PhoneNumber


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

    phones: Mapped[list[PhoneNumber]] = relationship(
        "PhoneNumber",
        backref="organization",
        cascade="all, delete-orphan",
    )

    building_id: Mapped[int] = mapped_column(
        ForeignKey("buildings.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )

    building: Mapped[Building] = relationship(
        "Building",
        back_populates="organizations",
    )

    activity: Mapped[list[Activity]] = relationship(
        "Activity",
        back_populates="organization",
        secondary=organization_activities,
    )
