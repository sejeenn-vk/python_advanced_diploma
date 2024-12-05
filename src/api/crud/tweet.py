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
        .filter(Tweet.user_id.in_(user.id for user in current_user.followed))
        .options(
            joinedload(Tweet.likes),
            # joinedload(Tweet.likes).subqueryload(Like.user),
            joinedload(Tweet.images),
        )
        .order_by(Tweet.created_at.desc())
    )
    test = await session.execute(
        select(Tweet)
        .filter(Tweet.user_id.in_(user.id for user in current_user.followed))
        .options(joinedload(Tweet.likes))

    )
    from sqlalchemy import func

    # # Сортировка по количеству адресов у пользователя
    # user_address_counts = session.query(User.name, func.count(Address.id).label('address_count')).join(
    #     Address).group_by(User.name).order_by('address_count').all()
    # сортировка по имени курса и преподавателю
    # tweets = session.query(Tweet).join(Student.courses).order_by(Course.name, Course.teacher).all()

    print(test.unique().all())
    return result.unique().scalars().all()
