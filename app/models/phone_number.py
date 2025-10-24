from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.organization import Organization


class PhoneNumber(Base):
    __tablename__ = "phone_numbers"

    organization_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        index=True,
    )

    number: Mapped[str] = mapped_column(
        String(15),
        unique=True,
        nullable=False,
    )

    organization: Mapped[Organization] = relationship(
        "Organization",
        back_populates="phone_numbers",
    )
