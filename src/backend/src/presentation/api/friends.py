from fastapi import APIRouter, Depends

from src.domain.schemas.friends import FriendSchemaAdd
from src.infrastructure.services.friends import FriendService
from .dependencies import friend_service

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.options.db import get_async_session


router = APIRouter(
	prefix='/friends',
	tags=['Friends'],
)
@router.post('/')
async def add_friend(
	data: FriendSchemaAdd,
	friend_service: FriendService = Depends(friend_service),
	session: AsyncSession = Depends(get_async_session)
):
	await friend_service.add_friend(session, data)
	return {'status': 'ok'}