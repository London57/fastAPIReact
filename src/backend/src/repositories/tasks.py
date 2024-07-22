from src.models.tasks import Task
from .base import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository):
    model = Task

    