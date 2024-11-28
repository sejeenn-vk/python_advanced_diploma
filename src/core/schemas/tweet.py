from typing import Optional

from pydantic import BaseModel, Field, ConfigDict
from .base import BaseSchema


class CreateTweet(BaseModel):
    """
    Схема для входных данных при добавлении нового твита
    """

    tweet_data: str = Field()
    tweet_media_ids: Optional[list[int]]

    # @field_validator("tweet_data", mode="before")
    # @classmethod
    # def check_len_tweet_data(cls, val: str) -> str | None:
    #     """
    #     Проверка длины твита с переопределением вывода ошибки в случае превышения
    #     """
    #     if len(val) > 280:
    #         raise CustomApiException(
    #             status_code=HTTPStatus.UNPROCESSABLE_ENTITY,  # 422
    #             detail=f"The length of the tweet should not exceed 280 characters. "
    #                    f"Current value: {len(val)}",
    #         )
    #
    #     return val

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
