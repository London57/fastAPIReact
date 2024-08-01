from src.infrastructure.db.repositories.base import AbstractRepository
from src.domain.schemas.user import UserSchemaAdd


class UserAuthService:
	def __init__(self, repo):
		self.user_repo: AbstractRepository = repo()

	async def register_user(self, form: UserSchemaAdd):
		data = form.model_dump()
		print('data in user_auth repo', data)
		self.user_repo.add_one(data)
		