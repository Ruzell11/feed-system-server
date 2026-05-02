from sqlalchemy.orm import Session
from app.models.refresh_token import RefreshToken


class TokenRepository:

    @staticmethod
    async def save_refresh_token(db: Session, user_id: int, token: str):
        rt = RefreshToken(user_id=user_id, token=token)
        db.add(rt)
        await db.commit()
        await db.refresh(rt)
        return rt
    
    @staticmethod
    async def get_token(db: Session, token: str):
        return await db.query(RefreshToken).filter(RefreshToken.token == token).first()
    

    @staticmethod
    async def delete_token(db: Session, token: str):
        await db.query(RefreshToken).filter(
            RefreshToken.token == token
        ).delete()
        await db.commit()