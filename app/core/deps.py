from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.core.config import config

security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, config.JWT_SECRET, algorithms=[config.ALGORITHM])
        print("PAYLOAD:", payload)  # 🔥 add this

        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")

        return int(user_id)

    except JWTError as e:
        print("JWT ERROR:", str(e))  # 🔥 add this
        raise HTTPException(status_code=401, detail="Invalid or expired token")