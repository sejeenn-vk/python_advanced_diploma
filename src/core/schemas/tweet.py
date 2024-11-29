from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict
from .base import BaseSchema
from .user import BaseUserSchema
from .like import LikeSchema


class CreateTweetSchema(BaseModel):
    """
    Схема для входных данных при добавлении нового твита
    """

    tweet_data: str = Field()
    tweet_media_ids: Optional[list[int]]

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,  # Использовать псевдоним вместо названия поля
    )


class TweetResponse(BaseSchema):
    """
    Схема для вывода id твита после публикации
    """
    id: int = Field(alias="tweet_id")
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,  # Использовать псевдоним вместо названия поля

    )


class TweetOutSchema(BaseModel):
    """
    Схема для вывода твита, автора, вложенных изображений и данных по лайкам
    """

    id: int
    tweet_data: str = Field(alias="content")
    user: BaseUserSchema = Field(alias="author")
    likes: List[LikeSchema]
    images: List[str] = Field(alias="attachments")

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,  # Использовать псевдоним вместо названия поля
    )


class TweetListSchema(BaseSchema):
    """
    Схема для вывода списка твитов
    """

    tweets: List[TweetOutSchema]
