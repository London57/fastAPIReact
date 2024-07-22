from fastapi import Depends

from src.auth.models.depends import get_user_db
from .manager import UserManager


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)