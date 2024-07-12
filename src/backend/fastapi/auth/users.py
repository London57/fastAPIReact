from fastapi_users import FastAPIUsers
import uuid

from .models.models import User
from .backend import auth_backend
from .managers.depends import get_user_manager

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_user = fastapi_users.current_user(active=True)
