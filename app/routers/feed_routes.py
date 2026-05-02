from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_db
from app.core.deps import get_current_user
from app.controllers.feed_controller import get_feed_controller

router = APIRouter(prefix="/feed", tags=["Feed"])


@router.get("/")
async def get_feed(
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_current_user),
    limit: int = Query(20, ge=1, le=50),
    offset: int = Query(0, ge=0)
):
    return await get_feed_controller(db, user_id, limit, offset)