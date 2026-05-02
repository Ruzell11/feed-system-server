from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import RefreshRequest, SignupRequest, LoginRequest
from app.services.auth_service import AuthService


def signup_controller(data: SignupRequest, db: Session):
    try:
        user = AuthService.signup(
            db,
            data.username,
            data.email,
            data.password
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


def login_controller(data: LoginRequest, db: Session):
    try:
        user = AuthService.login(
            db,
            data.email,
            data.password
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

def refresh_controller(data: RefreshRequest, db: Session):
    try:
        user = AuthService.refresh_token(
            db,
            data.refresh_token
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
def logout_controller(data: RefreshRequest, db: Session):
    try:
        user = AuthService.logout(
            db,
            data.refresh_token
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))