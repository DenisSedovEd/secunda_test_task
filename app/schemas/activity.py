from typing import List, Optional

from pydantic import BaseModel, Field


class ActivityBase(BaseModel):
    name: str
    parent_id: Optional[int] = None


class ActivityCreate(ActivityBase):
    pass


class ActivityResponse(ActivityBase):
    id: int
    children: List["ActivityResponse"] = Field(default_factory=list)

    class Config:
        from_attributes = True
