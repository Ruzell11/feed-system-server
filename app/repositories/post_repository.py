from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate


class PostRepository:

    @staticmethod
    async def create_post(db: Session, user_id: int, body: PostCreate):
        post = Post(user_id=user_id, content=body.content, title=body.title)
        db.add(post)
        await db.commit()
        await db.refresh(post)
        return post

    @staticmethod
    async def get_posts_by_user_ids(db: Session, user_ids: list[int]):
        return (
            await db.query(Post)
            .filter(Post.user_id.in_(user_ids))
            .order_by(Post.created_at.desc())
            .all()
        )