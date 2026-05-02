from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class Post(Base):
    __tablename__ = "posts"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"))
    content = mapped_column(String(280))

    user = relationship("User", back_populates="posts")