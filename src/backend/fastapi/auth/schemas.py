from typing import Annotated
from pydantic import BaseModel, EmailStr, field_validator, ValidationError, Field
from fastapi_users.schemas import BaseUserCreate, BaseUser
import uuid

class CreateUserSchema(BaseUserCreate):
	username: Annotated[str, Field(min_length=3)]
	repeat_password: str

	@staticmethod
	@field_validator('repeat_password')
	def validate_passwords(value, values):
		if value != values['password']: 
			return ValidationError(
					"passwords missmatch"
				)
		return value
		
class ReadUserSchema(BaseUser[uuid.UUID]):
	username: str
	