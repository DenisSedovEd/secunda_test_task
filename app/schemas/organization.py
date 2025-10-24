from pydantic import BaseModel
from app.models.organization import Organization


class OrganizationCreate(BaseModel):
    name: str
    phone_numbers: list[str] = []


class OrganizationResponse(BaseModel):
    name: str
