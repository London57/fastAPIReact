from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

import toml


config = toml.load("src/infrastructure/db/options/config.toml")
database_config = config.get("PostgreSQL")



driver = database_config.get("driver")
user = database_config.get("user")
password = database_config.get("password")
host = database_config.get("host")
port = database_config.get("port")
database_name = database_config.get("database_name")

engine = create_async_engine(f"postgresql+{driver}://{user}:{password}@{host}:{port}/{database_name}", echo=True)
async_session_maker = async_sessionmaker(engine)

async def get_async_session():
    async with async_session_maker() as session:
        yield session

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )

async def drop_tables():
   async with engine.begin() as conn:
       await conn.run_sync(Base.metadata.drop_all)