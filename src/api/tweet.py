from typing import Annotated

from fastapi import APIRouter, Depends, Security
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models import db_helper, User
from src.core.schemas.tweet import CreateTweet, TweetResponse
from src.utils.get_user import get_current_user
from src.api.crud.tweet import create_new_tweet

tweets_route = APIRouter(
    prefix="/api/tweets"
)


@tweets_route.post("", tags=["Написать новый твит"], response_model=TweetResponse)
async def create_new_tweet(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        tweet: CreateTweet,
        current_user: Annotated[User, Depends(get_current_user)],

):

    # Пишем твит
    tweet = await create_new_tweet(
        tweet=tweet, current_user=current_user, session=session
    )
    print(tweet)
    return {"tweet_id": tweet.id}

    # return {"result": "true", "tweet_id": 100500}


@tweets_route.get(
    ""
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
