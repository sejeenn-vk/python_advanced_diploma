from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.user import users_route
from src.api.tweet import tweets_route
from sqlalchemy import text
from src.core.models.db_helper import db_helper
from src.core.models.base import Base
import datetime


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(
            text("insert into users (name, api_key) values ('Евгений Воронцов', 'test')")
        )
        await conn.execute(
            text("insert into users (name, api_key) values ('Владимир Ульянов', 'lenin')")
        )
        await conn.execute(
            text("insert into users (name, api_key) values ('Александр Пушкин', 'pushkin')")
        )
        await conn.execute(
            text(f"insert into tweets (content, user_id, created_at) "
                 f"values ('Будь здоров!', 1, current_timestamp)")
        )
        await conn.execute(
            text(f"insert into tweets (content, user_id, created_at) "
                 f"values ('Всегда здоров!', 3, current_timestamp)")
        )
        await conn.execute(
            text(f"insert into tweets (content, user_id, created_at) "
                 f"values ('Ленин жил, Ленин жив, Ленин будет жить!', 2, current_timestamp)")
        )
    yield
    # await db_helper.dispose()

main_app = FastAPI(lifespan=lifespan)
main_app.include_router(users_route)
main_app.include_router(tweets_route)
