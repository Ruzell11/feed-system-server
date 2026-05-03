from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.refresh_token import RefreshToken


class TokenRepository:

    @staticmethod
    async def save_refresh_token(db: AsyncSession, user_id: int, token: str):
        rt = RefreshToken(user_id=user_id, token=token)
        db.add(rt)
        await db.commit()
        await db.refresh(rt)
        return rt
    
    @staticmethod
    async def get_token(db: AsyncSession, token: str):
        result = await db.execute(
            select(RefreshToken).where(RefreshToken.token == token)
    )
        return result.scalar_one_or_none()
        

    @staticmethod
    async def delete_token(db: AsyncSession, token: str):
        await db.execute(
            delete(RefreshToken).where(RefreshToken.token == token)
        )
        await db.commit()