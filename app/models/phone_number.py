from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.organization import Organization


class PhoneNumber(Base):
    __tablename__ = "phone_numbers"

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    number: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False,
    )

    organization: Mapped[Organization] = relationship(
        "Organization",
        back_populates="phone_numbers",
    )

    def __repr__(self) -> str:
        return f"PhoneNumber(id={self.id!r}, organization_id={self.organization_id!r}, number={self.number!r})"
