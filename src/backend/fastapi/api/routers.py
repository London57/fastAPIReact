from api.users import router as users_router
from api.tasks import router as tasks_router


all_routers = [
    users_router,
    tasks_router,
]