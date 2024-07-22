from .base import SQLAlchemyRepository
from src.models.friends import Friend
from src.db.db import async_session_maker


class FriendsRepository(SQLAlchemyRepository):
	model = Friend
											