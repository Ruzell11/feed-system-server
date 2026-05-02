from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.follow import Follow

class FollowRepository:

    @staticmethod
    async def follow(db: AsyncSession, follower_id: int, following_id: int):
        follow = Follow(
            follower_id=follower_id,
            following_id=following_id
        )

        db.add(follow)
        await db.commit()
        return follow
    
    @staticmethod
    async def unfollow(db: AsyncSession, follower_id: int, following_id: int):
        stmt = delete(Follow).where(
            Follow.follower_id == follower_id,
            Follow.following_id == following_id
        )

        await db.execute(stmt)
        await db.commit()

    @staticmethod
    async def get_following(db: AsyncSession, user_id: int):
        stmt = select(Follow).where(Follow.follower_id == user_id)
        result = await db.execute(stmt)
        return result.scalars().all()
    
    @staticmethod
    async def get_followers(db: AsyncSession, user_id: int):
        stmt = select(Follow).where(Follow.following_id == user_id)
        result = await db.execute(stmt)
        return result.scalars().all()