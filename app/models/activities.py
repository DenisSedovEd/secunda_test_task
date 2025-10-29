from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.organization import Organization


class Activity(Base):
    __tablename__ = "activities"
    __table_args__ = (
        UniqueConstraint("name", "parent_id", name="uq_activity_name_parent"),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey("activities.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
    )
    parent: Mapped["Activity | None"] = relationship(
        "Activity",
        back_populates="children",
        backref="sub_activities",
    )
    children: Mapped[list["Activity"]] = relationship(
        "Activity",
        back_populates="parent",
        cascade="all, delete-orphan",
    )
    organization: Mapped[list["Organization"]] = relationship(
        "Organization",
        secondary="organization_activities",
        back_populates="activities",
    )

    def __repr__(self) -> str:
        return f"Activity(id={self.id!r}, name={self.name!r}, parent_id={self.parent_id!r})"
