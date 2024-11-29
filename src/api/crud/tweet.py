from sqlalchemy import select
from sqlalchemy.orm import joinedload

from sqlalchemy.ext.asyncio import AsyncSession

from src.core.models import User, Tweet, Like
from src.core.schemas.tweet import CreateTweetSchema


async def create_new_tweet(
        session: AsyncSession,
        tweet_data: CreateTweetSchema,
        current_user: User,
) -> Tweet:
    """
    Создание нового твита в базе данных.
    :param session: AsyncSession
    :param tweet_data: schema CreateTweet
    :param current_user: model User
    :return:
    """
    tweet = Tweet(content=tweet_data.tweet_data, user_id=current_user.id)
    session.add(tweet)
    await session.commit()
    return tweet


async def get_all_tweets(
        session: AsyncSession,
        current_user: User,
):
    """
    Пользователь может получить ленту из твитов отсортированных в
    порядке убывания по популярности от пользователей, которых он
    читает.
    :param current_user:
    :param session:
    :return:
    """
    result = await session.execute(
        select(Tweet)
        .options(
            joinedload(Tweet.user),
            joinedload(Tweet.likes).subqueryload(Like.user),
            joinedload(Tweet.images),
        )
        .order_by(Tweet.created_at.desc())
    )
    return result.unique().scalars().all()
