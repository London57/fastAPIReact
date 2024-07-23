from src.repositories.base import AbstractRepository
from src.schemas.friends import FriendSchemaAdd


class FriendService:
	def __init__(self, friends_repository):
		self.friends_repo: AbstractRepository = friends_repository()
	
	async def add_friend(self, data: FriendSchemaAdd):
		data = data.model_dump()
		data['is_accept'] = False
		await self.friends_repo.add_one(data)
		
		