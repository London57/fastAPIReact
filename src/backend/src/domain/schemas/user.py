from pydantic import BaseModel

from uuid import UUID
from src.domain.value_objects import Email, Username, Hashed_password


class UserSchema(BaseModel):
	id: UUID
	username: Username
	email: Email
	hashed_password: Hashed_password

class UserSchemaAdd(BaseModel):
	username: Username
	email: Email
	password: Hashed_password

class UserLoginSchema(BaseModel):
	username_or_email: Username | Email
	password: Hashed_password