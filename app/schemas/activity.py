from typing import Optional, List

from pydantic import BaseModel


class ActivityBase(BaseModel):
    name: str
    parent_id: Optional[int] = None


class ActivityCreate(ActivityBase):
    pass


class ActivityResponse(ActivityBase):
    id: int
    children: List["ActivityResponse"] = []

    class Config:
        from_attributes = True
