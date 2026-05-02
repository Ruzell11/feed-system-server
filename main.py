from fastapi import FastAPI
from app.routers.auth_routes import router as auth_router

app = FastAPI()

app.include_router(auth_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Feed System API"}