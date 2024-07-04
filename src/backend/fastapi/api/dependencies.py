from repositories.tasks import TasksRepository
from repositories.users import UsersRepository
from services.tasks import TasksService
from services.users import UserService


def tasks_service():
    return TasksService(TasksRepository)

def users_service():
    return UserService(UsersRepository)