from src.domain.schemas.friends import FriendSchemaAdd

from src.application.interfaces.repositories import IFriendRepository


class FriendService:
	def __init__(self, friends_repository):
		self.friends_repo: IFriendRepository = friends_repository()


	async def add_friend(self, session, data: FriendSchemaAdd):
		data = data.model_dump()
		data['is_accept'] = False

		await self.friends_repo.add_one_friend(session, data)
		
		