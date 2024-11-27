from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.models import User
from src.core.schemas.user import CreateUser


async def get_user_by_api_key(
        session: AsyncSession,
        api_key,
) -> User:
    stmt = (select(User)
            .where(User.api_key == api_key)
            .options(joinedload(User.followers).load_only(User.id, User.name))
            .options(joinedload(User.followed).load_only(User.id, User.name))
            )
    result = await session.scalars(stmt)
    return result.unique().one()


async def get_user_by_user_id(
        session: AsyncSession,
        user_id,
) -> User:
    stmt = (select(User)
            .where(User.id == user_id)
            .options(joinedload(User.followers).load_only(User.id, User.name))
            .options(joinedload(User.followed).load_only(User.id, User.name))
            )
    result = await session.scalars(stmt)
    return result.unique().one()


async def create_user(
        session: AsyncSession,
        user_create: CreateUser,
) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    return user
