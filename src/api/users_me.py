from typing import Annotated

from fastapi import APIRouter, Header

from src.core.schemas.users import UsersMe

users_me = APIRouter(
    prefix="/api"
)


@users_me.get("/users/me", tags=["Users me"], response_model=UsersMe)
async def get_users_me(api_key: Annotated[str | None, Header()] = None):
    print(f"==============================={api_key}=================================")
    return {
        "result": "true",
        "user": {
            "id": 1,
            "name": "Евгений Воронцов",
            "followers": [{"id": 2, "name": "Николай Воронцов"}],
            "following": [{"id": 3, "name": "Татьяна Воронцова"}],
        },
    }
