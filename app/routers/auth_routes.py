from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.schemas.auth import SignupRequest, LoginRequest, AuthResponse, TokenResponse, RefreshRequest

from app.controllers.auth_controller import logout_controller, signup_controller, login_controller, refresh_controller

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/signup", response_model=AuthResponse)
async def signup(data: SignupRequest, db: Session = Depends(get_db)):
    return await signup_controller(data, db)


@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest, db: Session = Depends(get_db)):
    return await login_controller(data, db)

@router.post("/refresh")
async def refresh(data: RefreshRequest, db: Session = Depends(get_db)):
    return await refresh_controller(data, db)

@router.post("/logout")
async def logout(data: RefreshRequest, db: Session = Depends(get_db)):
    return await logout_controller(data, db)