from typing import Annotated

from fastapi import APIRouter, Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.schemas.users import UsersMe, CreateUser
from src.core.models.db_helper import db_helper
from src.api.crud import user as users_crud

users_me = APIRouter(
    prefix="/api"
)


@users_me.get("/users/me", tags=["Users me"], response_model=UsersMe)
async def get_users_me(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        api_key: Annotated[str | None, Header()] = None,
):
    user = await users_crud.get_user_by_api_key(session=session, api_key=api_key)
    data = {"result": "true", "user": {
        "id": user.id, "name": user.name,
        "followers": [], "following": []
    }}

    # print(f"_________________{user.followers}________________________________")

    return data


@users_me.post("", response_model=CreateUser)
async def create_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        user_create: CreateUser,
):
    user = await users_crud.create_user(session=session, user_create=user_create)
    return user
