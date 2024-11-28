from typing import Annotated

from fastapi import APIRouter, Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models import db_helper
from src.core.schemas.tweet import CreateTweet

tweets_route = APIRouter(
    prefix="/api"
)


@tweets_route.post(
    "/tweets"
)
async def create_new_tweet(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        # tweet_create: str = Header(),
):
    # print(tweet_create.encode())
    return {"result": "true", "tweet_id": 100500}


@tweets_route.get(
    "/tweets"
)
async def get_all_tweets(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        # tweet_create: CreateTweet,
):
    # /api/tweets?offset=1&limit=5 роут с пагинацией
    return {
        "result": "true",
        "tweets": [
            {
                "id": 100,
                "content": "Жили у бабуси, два весёлых гуся!",
                "attachments": [],
                "author": {
                    "id": 2,
                    "name": "Евгений Онегин",
                },
                "likes": [
                    {
                        "user_id": 1,
                        "name": "Николай Гоголь",
                    },
                    {
                        "user_id": 4,
                        "name": "Владимир Ульянов",
                    }
                ]
            },
            {
                "id": 101,
                "content": "Один серый другой белый, два веселых гуся!",
                "attachments": [],
                "author": {
                    "id": 5,
                    "name": "Александр Пушкин",
                },
                "likes": [
                    {
                        "user_id": 4,
                        "name": "Владимир Ульянов"
                    }
                ]
            }
        ],
    }
