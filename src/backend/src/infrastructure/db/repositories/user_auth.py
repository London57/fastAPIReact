from abc import ABCMeta
from src.infrastructure.db.models.user import User
from src.domain.schemas.user import UserSchemaAdd

from src.application.interfaces.repositories.user_auth import IUserAuthRepository
from .base import SQLAlchemyRepo

from sqlalchemy import insert, select, or_

from fastapi import HTTPException

from passlib import hash


class UserAuthRepository(SQLAlchemyRepo, IUserAuthRepository):
	model = User

	async def create_user(self, data: UserSchemaAdd):
		data_dict = data.model_dump()
		statement = insert(self.model).values(**data_dict)
		res = await self.session.execute(statement)
		self.session.commit()
		return res.lastrowid

	async def get_user_by_username(self, username: str):
		statement = select(self.model).where(self.model.username == username)
		res = await self.session.execute(statement)
		return res.first()

	async def authenticate_user(self, username_or_email, password):
		get_user_by_email = select(self.model).where(
			or_(
				self.model.email == username_or_email,
				self.model.username == username_or_email,
			)
		)
		user = await self.session.execute(get_user_by_email)
		
		user = user.first()

		if not user:
			raise HTTPException(400, "invalid username or email")
		
		if not hash.argon2.verify(password, self.model.hashed_password):
			raise HTTPException(400, 'invalid password')
		
		return user