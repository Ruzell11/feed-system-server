from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas.auth import SignupRequest, LoginRequest, AuthResponse, TokenResponse, RefreshRequest

from app.controllers.auth_controller import logout_controller, signup_controller, login_controller, refresh_controller

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=AuthResponse)
def signup(data: SignupRequest, db: Session = Depends(get_db)):
    return signup_controller(data, db)


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return login_controller(data, db)

@router.post("/refresh")
def refresh(data: RefreshRequest, db: Session = Depends(get_db)):
    return refresh_controller(data, db)

@router.post("/logout")
def logout(data: RefreshRequest, db: Session = Depends(get_db)):
    return logout_controller(data, db)