from fastapi import FastAPI
from app.routers.auth_routes import router as auth_router
from app.routers.post_routes import router as post_router
from app.routers.follow_routes import router as follow_router
from app.routers.feed_routes import router as feed_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.router.redirect_slashes = False

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",   # Next.js dev
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(post_router)
app.include_router(follow_router)
app.include_router(feed_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Feed System API"}