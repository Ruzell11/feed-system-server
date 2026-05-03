from app.core.queue import feed_queue
from app.repositories.post_repository import PostRepository
from app.schemas.post import PostCreate
from sqlalchemy.ext.asyncio import AsyncSession
from app.workers.feed_worker import process_feed_fanout

class PostService:

    @staticmethod
    async def create_post(db: AsyncSession, user_id: int, body: PostCreate):

        # 1. create post
        post = await PostRepository.create_post(db, user_id, body)

        # 2. push job to queue (NO FANOUT HERE ANYMORE)
        feed_queue.enqueue(
            process_feed_fanout,
            post.id,
            user_id
        )

        return {
            "message": "Post created",
            "post_id": post.id,
            "status": "processing_feed"
        }