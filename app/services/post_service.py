from sqlalchemy.orm import Session
from app.repositories.post_repository import PostRepository
from app.schemas.post import PostCreate


class PostService:

    @staticmethod
    async def create_post(db: Session, user_id: int, body: PostCreate):
        return await PostRepository.create_post(db, user_id, body)