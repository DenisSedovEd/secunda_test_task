from typing import List

from pydantic import BaseModel


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
