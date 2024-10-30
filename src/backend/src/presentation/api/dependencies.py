from src.infrastructure.db.repositories.friends import FriendsRepository
from src.infrastructure.services.friends import FriendService

from src.infrastructure.db.repositories.user_auth import UserAuthRepository
from src.infrastructure.services.user_auth import UserAuthService

from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.options.db import get_async_session


def friend_service():
    return FriendService(FriendsRepository)

def user_auth_service():
    return UserAuthService(UserAuthRepository)