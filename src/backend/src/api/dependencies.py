from src.repositories.tasks import TasksRepository
from src.services.tasks import TasksService


def tasks_service():
    print('dependencies')
    return TasksService(TasksRepository)
