from typing import Sequence

from models.activities import Activity
from models.building import Building
from models.organization import Organization, organization_activities
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


class DoesNotExist(Exception):
    pass


class OrganizationRepository:

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, org_id: int) -> Organization:
        """
        Информация об организации по ID
        :param org_id:
        :return:
        """
        result = await self._session.execute(
            select(Organization)
            .options(
                selectinload(Organization.building), selectinload(Organization.activity)
            )
            .where(Organization.id == org_id)
        )
        return result.scalar_one_or_none()

    # async def get_by_building(self, building_id: int) -> Organization | None:
    #     result = await self._session.execute(
    #         select(Organization)
    #         .options(
    #             selectinload(Organization.building), selectinload(Organization.activity)
    #         )
    #         .where(Organization.building_id == building_id)
    #     )
    #     return result.scalar_one_or_none()

    async def get_by_activity_ids(
        self, activity_ids: list[int]
    ) -> Sequence[Organization]:
        """
        Список организаций по виду деятельности
        :param activity_ids:
        :return:
        """
        result = await self._session.execute(
            select(Organization)
            .join(organization_activities)
            .where(organization_activities.c.activity_id.in_(activity_ids))
            .options(
                selectinload(Organization.building), selectinload(Organization.activity)
            )
        )
        return result.scalars().all()

    async def search_by_name(self, name: str) -> Sequence[Organization] | None:
        """
        Поиск организации по названию
        :param name:
        :return:
        """
        result = await self._session.execute(
            select(Organization)
            .where(Organization.name.ilike(f"%{name}%"))
            .options(
                selectinload(Organization.building).selectinload(Organization.activity)
            )
        )
        return result.scalars().all()


class BuildingRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_with_orgs(self, building_id: int) -> list[Organization] | None:
        """
        Список всех организаций в конкретном здании
        :param building_id:
        :return:
        """
        result = await self._session.execute(
            select(Building)
            .options(selectinload(Building.organization))
            .where(Organization.building_id == building_id)
        )
        organizations = result.scalars().all()
        return organizations if organizations else None

    async def get_all(self) -> Sequence[Building]:
        result = await self._session.execute(select(Building))
        return result.scalars().all()


class ActivityRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_tree(self):
        """
        Список деятельностей (деревом)
        :return:
        """
        result = await self._session.execute(select(Activity).order_by(Activity.id))
        activities = result.scalars().all()
        activity_map = {a.id: a for a in activities}
        roots = []
        for a in activities:
            if a.parent_id is None:
                roots.append(a)
            elif a.parent_id in activity_map:
                activity_map[a.parent_id].children.append(a)
        return roots
