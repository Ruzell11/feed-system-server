from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import get_db
from app.core.deps import get_current_user
from app.services.post_service import PostService
from app.schemas.post import PostCreate

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/")
async def create_post_controller(
    body: PostCreate,
     db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_current_user),
   
):
    return await PostService.create_post(db, user_id, body)