from typing import List

from pydantic import BaseModel


class User(BaseModel):
    id: int = 1
    name: str = "John Doe"
    followers: List["User"] = [
        {"id": 2, "name": "Jack Black"},
        {"id": 3, "name": "Samanta Fox"}
    ]
    following: List["User"] = [{"id": 3, "name": "Samanta Fox"}]


class UsersMe(BaseModel):
    result: bool = "true"
    user: User


class CreateUser(BaseModel):
    name: str = "John Doe"
    followers: List["User"] = []
    followed: List["User"] = []
    api_key: str
