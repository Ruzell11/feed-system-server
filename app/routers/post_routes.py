from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.core.deps import get_current_user
from app.controllers.post_controller import create_post_controller
from app.schemas.post import PostCreate

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/")
async def create_post(
    body: PostCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return await create_post_controller(body, db, user_id)