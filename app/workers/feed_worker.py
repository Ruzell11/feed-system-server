import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# CREATE ONE GLOBAL LOOP
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


from app.core.db import AsyncSessionLocal
from app.repositories.follow_repository import FollowRepository
from app.repositories.feed_repository import FeedRepository


def process_feed_fanout(post_id: int, user_id: int):
    # SAME loop
    loop.run_until_complete(_process(post_id, user_id))


async def _process(post_id: int, user_id: int):
    async with AsyncSessionLocal() as db:

        followers = await FollowRepository.get_followers(db, user_id)

        for follower in followers:
            await FeedRepository.add_to_feed(
                db,
                user_id=follower.follower_id,
                post_id=post_id
            )

        await FeedRepository.add_to_feed(
            db,
            user_id=user_id,
            post_id=post_id
        )

        await db.commit()