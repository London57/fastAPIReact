from abc import ABCMeta
from src.infrastructure.db.models.user import User
from src.domain.schemas.user import UserSchemaAdd, UserSchema

from src.application.interfaces.repositories import IUserAuthRepository
from .base import SQLAlchemyRepo

from sqlalchemy import insert, select, or_

from passlib import hash

from fastapi import FastAPI, Depends, HTTPException, status, Security
from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials


access_security = JwtAccessBearer(secret_key="very_secret_key")

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
			return False, "invalid username or email"
		
		if not hash.argon2.verify(password, self.model.hashed_password):
			return False, "invalid password"
		
		return access_security.create_access_token(
				subject=UserSchema(user).model_dump()
			)
