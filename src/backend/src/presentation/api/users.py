# from typing import Annotated

# from fastapi import APIRouter, Depends

# from src.auth.users import current_active_user
# from src.auth.models.models import User


# router = APIRouter(
#     prefix="/get_user_info",
#     tags=["Tasks"],
# )

# @router.get('/')
# async def get_user_info(
#   user: User = Depends(current_active_user),
# ):
# 	return {'user': user}