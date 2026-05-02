from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.post_repository import PostRepository
from app.repositories.follow_repository import FollowRepository
from app.repositories.feed_repository import FeedRepository
from app.schemas.post import PostCreate


class PostService:

    @staticmethod
    async def create_post(
        db: AsyncSession,
        user_id: int,
        body: PostCreate
    ):
        # 1. Create post
        post = await PostRepository.create_post(
            db,
            user_id,
            body
        )

        # 2. Get followers (social graph layer)
        followers = await FollowRepository.get_followers(db, user_id)

        # 3. Fan-out to feeds (precomputed feed system)
        for follower in followers:
            await FeedRepository.add_to_feed(
                db=db,
                user_id=follower.follower_id,
                post_id=post.id
            )

        # 4. Add post to own feed (important for UX consistency)
        await FeedRepository.add_to_feed(
            db=db,
            user_id=user_id,
            post_id=post.id
        )

        # 5. Return enriched response (future-ready)
        return {
            "post": post,
            "feed_updated": True,
            "fanout_count": len(followers) + 1
        }