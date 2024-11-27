from pydantic import BaseModel, ConfigDict, Field


class Follow(BaseModel):
    id: int = 2
    name: str = "Александр Пушкин"


class User(BaseModel):
    id: int = 1
    name: str = "Лев Толстой"
    followers: list[Follow]
    following: list[Follow]


class UsersMe(BaseModel):
    result: bool = "true"
    user: User


class CreateUser(BaseModel):
    name: str = Field(default="Имя Фамилия")
    api_key: str = Field(default="api_key должен быть уникальным")


class UserRead(CreateUser):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
