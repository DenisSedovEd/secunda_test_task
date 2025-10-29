from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from app.repositories import BuildingRepository

router = APIRouter()


@router.get("/organizations/{building_id}")
async def get_organization_in_building(
    building_id: int, db: AsyncSession = Depends(get_session)
):
    repo = BuildingRepository(db)
    organizations = await repo.get_with_orgs(building_id)
    if not organizations:
        raise HTTPException(
            status_code=404, detail="No organizations found in this building"
        )

    return organizations
