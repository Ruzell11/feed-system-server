from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)

    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )

    password: Mapped[str] = mapped_column(
        String(255), nullable=False
    )

    # relationships (prepare for later)
    posts = relationship("Post", back_populates="user")

    following = relationship(
        "Follow",
        foreign_keys="Follow.follower_id",
        back_populates="follower"
    )

    followers = relationship(
        "Follow",
        foreign_keys="Follow.following_id",
        back_populates="following"
    )