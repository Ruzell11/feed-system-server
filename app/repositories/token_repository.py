from sqlalchemy.orm import Session
from app.models.refresh_token import RefreshToken


class TokenRepository:

    @staticmethod
    def save_refresh_token(db: Session, user_id: int, token: str):
        rt = RefreshToken(user_id=user_id, token=token)
        db.add(rt)
        db.commit()
        return rt
    
    @staticmethod
    def get_token(db: Session, token: str):
        return db.query(RefreshToken).filter(RefreshToken.token == token).first()
    

    @staticmethod
    def delete_token(db: Session, token: str):
        db.query(RefreshToken).filter(
            RefreshToken.token == token
        ).delete()
        db.commit()