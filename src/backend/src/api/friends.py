from fastapi import APIRouter, Depends

from src.schemas.friends import FriendSchemaAdd
from src.services.friends import FriendService
from .dependencies import friend_service


router = APIRouter(
	prefix='/friends',
	tags=['Friends'],
)

@router.post('/')
async def add_friend(
	data: FriendSchemaAdd,
	friend_service: FriendService = Depends(friend_service),
):
	await friend_service.add_friend(data)
	return {'status': 'ok'}