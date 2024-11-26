from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.users_me import users_me

from src.core.models.db_helper import db_helper
from src.core.models.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        # await conn.run_sync(Base.metadata.create_all)
    yield
    # await db_helper.dispose()

main_app = FastAPI(lifespan=lifespan)
main_app.include_router(users_me)
