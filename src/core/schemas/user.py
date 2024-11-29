from pydantic import BaseModel, ConfigDict, Field


class BaseUserSchema(BaseModel):
    id: int = 2
    name: str = "Александр Пушкин"
    model_config = ConfigDict(
        from_attributes=True,  # Автоматическое преобразование данных ORM-модели в объект схемы для сериализации
        populate_by_name=True,  # Использовать псевдоним вместо названия поля
    )


class UserFullSchema(BaseModel):
    id: int = 1
    name: str = "Лев Толстой"
    followers: list[BaseUserSchema]
    following: list[BaseUserSchema]


class UsersMe(BaseModel):
    result: bool = "true"
    user: UserFullSchema


class CreateUser(BaseModel):
    name: str = Field(default="Имя Фамилия")
    api_key: str = Field(default="api_key должен быть уникальным")


class UserRead(CreateUser):
    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int
