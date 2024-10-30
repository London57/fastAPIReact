from .friends import router as friend_router
from .auth import auth_router

all_routers = [
	friend_router,
	auth_router,
]