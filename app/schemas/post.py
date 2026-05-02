from pydantic import BaseModel, EmailStr


class PostCreate(BaseModel):
    content: str
    title: str
