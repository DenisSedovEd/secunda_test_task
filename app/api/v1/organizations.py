from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from app.repositories import OrganizationRepository

router = APIRouter()


@router.get("{org_id}")
async def get_organization(org_id: int, db: AsyncSession = Depends(get_session)):
    repo = OrganizationRepository(db)
    org = await repo.get_by_id(org_id)
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org


@router.get("/search")
async def search_organization_by_name(
    name: str = Query(..., min_length=1), db: AsyncSession = Depends(get_session)
):
    repo = OrganizationRepository(db)
    return await repo.search_by_name(name)
