from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


engine = create_async_engine("sqlite+aiosqlite://sqlite.db")
async_session_maker = async_sessionmaker(engine)

class Base(DeclarativeBase):
    pass