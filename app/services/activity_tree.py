from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession


async def get_subtree_ids(
    session: AsyncSession, root_id: int, max_depth: int = 3
) -> list[int]:
    query = text(
        """
        WITH RECURSIVE tree AS (
            SELECT id, 0 AS depth FROM activities WHERE id = :root_id
            UNION ALL
            SELECT a.id, t.depth + 1 FROM activities a
            JOIN tree t ON a.parent_id = t.id WHERE t.depth < :max_depth
        )
        SELECT id FROM tree
    """
    )
    result = await session.execute(query, {"root_id": root_id, "max_depth": max_depth})
    return [row[0] for row in result.fetchall()]
