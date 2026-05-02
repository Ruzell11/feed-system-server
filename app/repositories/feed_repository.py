from sqlalchemy.ext.asyncio import AsyncSession
from app.models.feed import Feed
from app.models.post import Post
from sqlalchemy import select


class FeedRepository:

    @staticmethod
    async def add_to_feed(db: AsyncSession, user_id: int, post_id: int):
        feed = Feed(user_id=user_id, post_id=post_id)

        db.add(feed)
        await db.commit()
        return feed
    
    @staticmethod
    async def get_feed(
        db: AsyncSession,
        user_id: int,
        limit: int,
        offset: int
    ):
        stmt = (
            select(Post)
            .join(Feed, Feed.post_id == Post.id)
            .where(Feed.user_id == user_id)
            .order_by(Feed.created_at.desc())
            .limit(limit)
            .offset(offset)
        )

        result = await db.execute(stmt)
        return result.scalars().all()