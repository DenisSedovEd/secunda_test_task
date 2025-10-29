from typing import TYPE_CHECKING, List

from pydantic import BaseModel

if TYPE_CHECKING:
    from app.models.activities import Activity
    from app.models.building import Building


class OrganizationBase(BaseModel):
    name: str
    phones: list[str]
    building_id: int
    activity_ids: list[str]


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationResponse(OrganizationBase):
    id: int
    building: "Building"
    activities: List["Activity"]

    class Config:
        from_attributes = True
