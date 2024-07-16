from fastapi_users import FastAPIUsers
import uuid

from .models.models import User
from .backend import auth_backend
from .manager.depends import get_user_manager

fastapiUsers = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])

current_active_user = fastapiUsers.current_user(active=True)
