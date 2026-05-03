from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.auth import RefreshRequest, SignupRequest, LoginRequest
from app.services.auth_service import AuthService


async def signup_controller(data: SignupRequest, db: AsyncSession):
    try:
        user = await AuthService.signup(
            db,
            data.username,
            data.email,
            data.password
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


async def login_controller(data: LoginRequest, db: AsyncSession):
    try:
        user = await AuthService.login(
            db,
            data.email,
            data.password
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

async def refresh_controller(data: RefreshRequest, db: AsyncSession):
    try:
        user = await AuthService.refresh_token(
            db,
            data.refresh_token
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
async def logout_controller(data: RefreshRequest, db: AsyncSession):
    try:
        user = await AuthService.logout(
            db,
            data.refresh_token
        )
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))