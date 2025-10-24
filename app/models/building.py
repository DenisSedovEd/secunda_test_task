from typing import TYPE_CHECKING

from sqlalchemy import String, DECIMAL, Numeric, UniqueConstraint
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.organization import Organization


class Building(Base):
    __tablename__ = "buildings"
    __table_args__ = (
        UniqueConstraint(
            "latitude", "longitude", name="uq_building_latitude_longitude"
        ),
    )

    address: Mapped[str] = mapped_column(
        String(200),
        unique=True,
        nullable=False,
    )
    latitude: Mapped[DECIMAL] = mapped_column(
        Numeric(9, 6),
        nullable=False,
    )
    longitude: Mapped[DECIMAL] = mapped_column(
        Numeric(9, 6),
        nullable=False,
    )
    organization: Mapped["Organization"] = relationship(
        "Organization",
        backref="building",
    )

    def __repr__(self):
        return f"Building(id={self.id!r}, address={self.address!r}, latitude={self.latitude!r}, longitude={self.longitude!r})"
