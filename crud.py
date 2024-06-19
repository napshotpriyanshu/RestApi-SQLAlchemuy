from models import Note
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from models import Note

class CRUD:
    async def get_all(self, async_session:async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            statement = select(Note).order_by(Note.id)

            result = await session.execute(statement)

            return result.scalars()