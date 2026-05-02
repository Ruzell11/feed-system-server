from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.core.security import create_access_token, create_refresh_token, hash_password, verify_password
from app.repositories.token_repository import TokenRepository
from jose import jwt, JWTError
from app.core.config import config


class AuthService:

    @staticmethod
    async def signup(db: Session, username: str, email: str, password: str):
        existing = await UserRepository.get_by_email(db, email)
        if existing:
            raise Exception("Email already exists")

        return await UserRepository.create_user(
            db,
            username,
            email,
            hash_password(password)
    )


    @staticmethod
    async def login(db: Session, email: str, password: str):
        user = await UserRepository.get_by_email(db, email)

        if not user or not verify_password(password, user.password):
            raise Exception("Invalid credentials")

        access_token = create_access_token({"sub": str(user.id)})
        refresh_token = create_refresh_token({"sub": str(user.id)})

        await TokenRepository.save_refresh_token(db, user.id, refresh_token)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }
    
    @staticmethod
    async def refresh_token(db: Session, refresh_token: str):
        try:
            payload = jwt.decode(refresh_token, config.JWT_SECRET, algorithms=[config.ALGORITHM])
            user_id = payload.get("sub")

            if not user_id:
                raise Exception("Invalid token")

            # check if token exists in DB (revocation check)
            stored = await TokenRepository.get_token(db, refresh_token)
            if not stored:
                raise Exception("Token revoked")

            new_access_token = create_access_token({"sub": user_id})

            return {
                "access_token": new_access_token,
                "token_type": "bearer"
            }

        except JWTError:
            raise Exception("Invalid refresh token")
        
    @staticmethod
    async def logout(db: Session, refresh_token: str):
        await TokenRepository.delete_token(db, refresh_token)
        return {"message": "Logged out"}