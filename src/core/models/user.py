from typing import List

from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Table, Column, Integer, ForeignKey


followers_tbl = Table(
    'followers_tbl',
    Base.metadata,
    Column(
        'follower_id', Integer, ForeignKey('users.id'), primary_key=True
    ),
    Column(
        'followed_id', Integer, ForeignKey('users.id'), primary_key=True
    ),
)


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    api_key: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    followers: Mapped[List["User"]] = relationship(
        "User",
        secondary=followers_tbl,
        primaryjoin=followers_tbl.c.followed_id == id,
        secondaryjoin=followers_tbl.c.follower_id == id,
        back_populates="followed",
    )
    followed: Mapped[List["User"]] = relationship(
        "User",
        secondary=followers_tbl,
        primaryjoin=followers_tbl.c.follower_id == id,
        secondaryjoin=followers_tbl.c.followed_id == id,
        back_populates="followers",
    )
