from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.models import User
from src.core.schemas.users import CreateUser


async def get_user_by_api_key(
        session: AsyncSession,
        api_key,
) -> User:
    stmt = select(User).where(User.api_key == api_key)
    result = await session.scalars(stmt)
    return result.one()


async def create_user(
        session: AsyncSession,
        user_create: CreateUser,
) -> User:
    user = User(**user_create.model_dump())
    session.add(user)
    await session.commit()
    # await session.refresh(user)
    return user
