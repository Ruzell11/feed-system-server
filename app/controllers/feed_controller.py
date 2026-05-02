from sqlalchemy.ext.asyncio import AsyncSession
from app.services.feed_service import FeedService


async def get_feed_controller(
    db: AsyncSession,
    user_id: int,
    limit: int = 20,
    offset: int = 0
):
    return await FeedService.get_feed(db, user_id, limit, offset)