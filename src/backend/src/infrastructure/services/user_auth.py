from src.infrastructure.db.repositories.base import SQLAlchemyRepo
from src.application.interfaces.services import IUserAuthService

from src.domain.schemas.user import UserSchemaAdd


class UserAuthService:
	def __init__(self, repo):
		self.user_repo: SQLAlchemyRepo = repo()

	async def register_user(self, form: UserSchemaAdd):
		data = form.model_dump()
		print('data in user_auth repo', data)
		self.user_repo.add_one(data)
		