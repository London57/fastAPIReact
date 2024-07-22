from src.models.friends import Friend
from src.db.db import engine, Base

async def create_tables():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)
		await conn.run_sync(Friend.metadata.create_all)