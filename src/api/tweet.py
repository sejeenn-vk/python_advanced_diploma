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
async def create_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        # tweet_create: CreateTweet,
):

    return {"result": "true", "tweet_id": 100500}


@tweets_route.get(
    "/tweets"
)
async def create_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        # tweet_create: CreateTweet,
):

    return {
        "result": "true",
        "tweets": [
            {
                "id": 100,
                "content": "Жили у бабуси, два весёлых гуся!",
                "attachments": []
            }
        ],
        "author": {
            "id": 5,
            "name": "George Bush",
        },
        "likes": [
            {
                "user_id": 1,
                "name": "Bill Clinton"
            }
        ]
    }

# {
# “result”: true,
# "tweets": [
# {
# "id": int,
# "content": string,
# "attachments" [
# link_1, // relative?
# link_2,
# ...
# ]
# "author": {
# "id": int
# "name": string
# }
# “likes”: [
# {
# “user_id”: int,
# “name”: string
# }
# ]
# },
# ...,
# ]
# }