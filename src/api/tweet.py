from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models import db_helper, User
from src.core.schemas.tweet import CreateTweetSchema, TweetResponse, TweetListSchema
from src.api.crud.get_user import get_current_user
from src.api.crud import tweet as tweet_crud

tweets_route = APIRouter(
    prefix="/api/tweets"
)


@tweets_route.post("", tags=["Написать новый твит"], response_model=TweetResponse)
async def create_new_tweet(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        tweet_data: CreateTweetSchema,
        current_user: Annotated[User, Depends(get_current_user)],

):
    # Пишем твит
    tweet = await tweet_crud.create_new_tweet(
        tweet_data=tweet_data, current_user=current_user, session=session
    )
    return {"tweet_id": tweet.id}


@tweets_route.get(
    "",
    response_model=TweetListSchema,
    status_code=200,
)
async def get_all_tweets(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        current_user: Annotated[User, Depends(get_current_user)],
):
    tweets = await tweet_crud.get_all_tweets(session=session, current_user=current_user)
    return {"tweets": tweets}
