from src.infrastructure.db.repositories.base import SQLAlchemyRepo
from src.application.interfaces.services import IUserAuthService

from passlib import hash

from src.domain.schemas.user import UserSchema, UserSchemaAdd, UserLoginSchema

from backend.src.infrastructure.security.is_authenticated import access_security

from src.application.interfaces.repositories import IUserAuthRepository


class UserAuthService:
	def __init__(self, repo):
		self.user_repo: IUserAuthRepository = repo()

	async def register_user(self, form: UserSchemaAdd):
		data = form.model_dump()
		print('data in user_auth repo', data)
		return self.user_repo.create_user(data)
		
	async def authenticate_user(self, form: UserLoginSchema):
		user = self.user_repo.get_user_by_email_or_username(form.username_or_email)

		if not user:
			return False, "invalid username or email"
		
		if not hash.argon2.verify(form.password, self.user_repo.model.hashed_password):
			return False, "invalid password"
		
		return access_security.create_access_token(
				subject=UserSchema(user).model_dump()
			)
