from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.feed_repository import FeedRepository


class FeedService:

    @staticmethod
    async def get_feed(
        db: AsyncSession,
        user_id: int,
        limit: int = 20,
        offset: int = 0
    ):
        return await FeedRepository.get_feed(db, user_id, limit, offset)