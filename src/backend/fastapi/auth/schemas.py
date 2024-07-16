from typing import Annotated
from pydantic import BaseModel, EmailStr, field_validator, ValidationError, Field
from fastapi_users.schemas import BaseUserCreate, BaseUser
import uuid

class CreateUserSchema(BaseUserCreate):
	username: Annotated[str, Field(min_length=3)]

class ReadUserSchema(BaseUser[uuid.UUID]):
    pass