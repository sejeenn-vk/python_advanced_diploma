from typing import Annotated

from fastapi import APIRouter, Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.schemas.user import UsersMe, CreateUser, UserRead
from src.core.models.db_helper import db_helper
from src.api.crud import user as users_crud

users_route = APIRouter(
    prefix="/api"
)


@users_route.get("/users/me", tags=["Users me"], response_model=UsersMe)
async def get_users_me(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        api_key:    Annotated[str | None, Header()] = None,
):
    user = await users_crud.get_user_by_api_key(session=session, api_key=api_key)
    data = {"result": "true", "user": {
        "id": user.id, "name": user.name,
        "followers": [{"id": x.id, "name": x.name} for x in user.followers],
        "following": [{"id": x.id, "name": x.name} for x in user.followed]
    }}
    return data


@users_route.get("/users/{user_id}", response_model=UsersMe)
async def get_user_by_id(
        session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
        user_id: int,
):
    user = await users_crud.get_user_by_user_id(session=session, user_id=user_id)
    data = {"result": "true", "user": {
        "id": user.id, "name": user.name,
        "followers": [{"id": x.id, "name": x.name} for x in user.followers],
        "following": [{"id": x.id, "name": x.name} for x in user.followed]
    }}
    return data


@users_route.post(
    "/users/me",
    tags=["Создать нового пользователя"],
    response_model=UserRead
)
async def create_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        user_create: CreateUser,
):
    user = await users_crud.create_user(session=session, user_create=user_create)
    return user
