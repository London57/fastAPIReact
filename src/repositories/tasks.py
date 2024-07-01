from models.tasks import Tasks
from .base import SQLAlchemyRepository


class TasksRepository(SQLAlchemyRepository):
    model = Tasks

    