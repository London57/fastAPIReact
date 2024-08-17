from fastapi import APIRouter, Depends

from src.infrastructure.services.user_auth import UserAuthService

from src.domain.schemas.user import UserSchemaAdd, UserLoginSchema

from .dependencies import user_auth_service

auth_router = APIRouter(
	prefix='/auth',
	tags=['Auth'],
)

@auth_router('/registration')
async def registration(
	form_data: UserSchemaAdd,
	user_auth_service: UserAuthService = Depends(user_auth_service),
):
	return user_auth_service.register_user(form_data)

@auth_router('/login')
async def login(
	form_data: UserLoginSchema,
	user_auth_service: UserAuthService = Depends(user_auth_service),
):
	return user_auth_service.authenticate_user(form_data) #token