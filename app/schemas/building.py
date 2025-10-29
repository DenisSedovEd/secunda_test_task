from pydantic import BaseModel, Field


class BuildingBase(BaseModel):
    address: str
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)


class BuildingCreate(BuildingBase):
    pass


class BuildingResponse(BaseModel):
    building_id: int

    class Config:
        from_attributes = True
