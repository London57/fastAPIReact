from .base import SQLAlchemyRepo
from src.application.interfaces.repositories.friends import IFriendRepository

from src.domain.schemas.friends import FriendSchemaAdd
from src.infrastructure.db.models.friends import Friend

from sqlalchemy import insert


class FriendsRepository(SQLAlchemyRepo, IFriendRepository):
	model = Friend

	async def add_one_friend(self, data: FriendSchemaAdd):
		data_dict = data.model_dump()
		statement = insert(self.model).values(**data_dict)
		res = await self.session.execute(statement)
		await self.session.commit()
		return res.lastrowid
