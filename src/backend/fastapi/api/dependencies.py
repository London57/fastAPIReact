from repositories.tasks import TasksRepository
from services.tasks import TasksService


def tasks_service():
    return TasksService(TasksRepository)
