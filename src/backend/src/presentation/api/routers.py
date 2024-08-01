from src.api.tasks import router as tasks_router
from .friends import router as friend_router
from .users import router as users_router

all_routers = [
  tasks_router,
	friend_router,
	users_router,
]