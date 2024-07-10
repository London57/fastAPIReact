from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from sqlalchemy.orm import Session

engine = create_async_engine("sqlite+aiosqlite:///sqlite.db", echo=True)
async_session_maker = async_sessionmaker(engine)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


async def create_tables():
    async with engine.begin() as conn:
       await conn.run_sync(Base.metadata.create_all)

async def drop_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Base.metadata.drop_all)