from typing import Optional, Annotated

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import APIKeyHeader
from fastapi import Security, Depends
from sqlalchemy.orm import joinedload
from starlette.requests import Request

from src.core.models import db_helper, User


class APITokenHeader(APIKeyHeader):
    """
    Проверка и извлечение токена из header
    """

    async def __call__(self, request: Request) -> Optional[str]:
        api_key = request.headers.get(self.model.name)
        return api_key


TOKEN = APITokenHeader(name="api-key")


async def get_current_user(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),],
        token: str = Security(TOKEN)
):
    stmt = select(User).where(User.api_key == token).options(joinedload(User.followed).load_only(User.id, User.name))
    result = await session.scalars(stmt)
    user = result.unique().one()

    return user
