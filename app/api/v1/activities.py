from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from app.repositories import ActivityRepository, OrganizationRepository
from app.services.activity_tree import get_subtree_ids

router = APIRouter()


@router.get("/")
async def list_activities(db: AsyncSession = Depends(get_session)):
    repo = ActivityRepository(db)
    return await repo.get_tree()


@router.get("/organizations/{activity_id}")
async def get_orgs_by_activity(
    activity_id: int, db: AsyncSession = Depends(get_session)
):
    repo = OrganizationRepository(db)
    ids = await get_subtree_ids(db, activity_id)
    return await repo.get_by_activity_ids(ids)
