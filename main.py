from fastapi import FastAPI
from app.routers.auth_routes import router as auth_router
from app.routers.post_routes import router as post_router
from app.routers.follow_routes import router as follow_router
app = FastAPI()

app.include_router(auth_router)
app.include_router(post_router)
app.include_router(follow_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Feed System API"}