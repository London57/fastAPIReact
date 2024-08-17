from .friends import router as friend_router
from .users import router as users_router

all_routers = [
	friend_router,
	users_router,
]