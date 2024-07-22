from src.repositories.base import AbstractRepository


class FriendService:
	def __init__(self, friends_repository: AbstractRepository):
		self.friends_repo = friends_repository()
	
	# async def get_

