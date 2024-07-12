import uuid
from typing import Optional, Union

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from auth.models.models import User
from auth.schemas import CreateUserSchema

SECRET = "SECRET"


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
    
    async def validate_password(self, password: str, user: Union[User, CreateUserSchema]) -> None:
        return await super().validate_password(password, user)