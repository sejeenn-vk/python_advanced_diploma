import datetime

from sqlalchemy import insert
from src.core.models.likes import Like
from src.core.models.user import User, followers_tbl
from src.core.models.tweet import Tweet

users_data = [
    {"name": 'Евгений Воронцов', "api_key": "test"},
    {"name": 'Владимир Ульянов', "api_key": "lenin"},
    {"name": 'Александр пушкин', "api_key": "pushkin"},
]

tweet_data = [
    {"content": "Будь здоров!", "user_id": 1, "created_at": datetime.datetime.now()},
    {"content": "Всегда здоров!", "user_id": 3, "created_at": datetime.datetime.now()},
    {
        "content": "Ленин жил, Ленин жив, Ленин будет жить!",
        "user_id": 2, "created_at": datetime.datetime.now()
    },
    {"content": "Я помню чудное мгновенье...", "user_id": 3, "created_at": datetime.datetime.now()},
]

like_data = [
    {"user_id": 1, "tweet_id": 2},
    {"user_id": 2, "tweet_id": 2},
    {"user_id": 3, "tweet_id": 2},
    {"user_id": 1, "tweet_id": 3},
    {"user_id": 2, "tweet_id": 3},
    {"user_id": 1, "tweet_id": 4},

]

followed_data = [
    {"follower_id": 1, "followed_id": 2},
    {"follower_id": 1, "followed_id": 3},

]


async def insert_data(conn):
    await conn.execute(insert(User), users_data)
    await conn.execute(insert(Tweet), tweet_data)
    await conn.execute(insert(Like), like_data)
    await conn.execute(insert(followers_tbl), followed_data)
