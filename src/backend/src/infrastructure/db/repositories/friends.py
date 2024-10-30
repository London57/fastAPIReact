from src.application.interfaces.repositories.friends import IFriendRepository

from src.domain.schemas.friends import FriendSchemaAdd
from src.infrastructure.db.models.friends import Friend

from sqlalchemy import insert


class FriendsRepository(IFriendRepository):
	model = Friend


	async def add_one_friend(self, session, data: FriendSchemaAdd):
		print(data)
		statement = insert(self.model).values(**data)
		res = await session.execute(statement)
		
		await session.commit()
		return res.lastrowid
