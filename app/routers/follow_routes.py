from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.deps import get_current_user
from app.core.db import get_db
from app.controllers.follow_controller import (
    follow_user_controller,
    unfollow_user_controller,
    get_followers_controller,
    get_following_controller
)

router = APIRouter(prefix="/follow", tags=["Follow"])

@router.post("/{target_id}")
async def follow_user(
    target_id: int,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return await follow_user_controller(db, user_id, target_id)


@router.delete("/{target_id}")
async def unfollow_user(
    target_id: int,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return await unfollow_user_controller(db, user_id, target_id)


@router.get("/followers")
async def get_followers(
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return await get_followers_controller(db, user_id)


@router.get("/following")
async def get_following(
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_current_user)
):
    return await get_following_controller(db, user_id)