from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Row

from models.organization import Organization


class DoesNotExist(Exception):
    pass


class OrganizationRepository:

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, org_id: int) -> Organization:
        return await self._session.
