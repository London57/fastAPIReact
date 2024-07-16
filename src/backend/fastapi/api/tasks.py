from typing import Annotated

from fastapi import APIRouter, Depends

from api.dependencies import tasks_service
from schemas.tasks import TaskSchemaAdd
from services.tasks import TasksService

from auth.users import current_active_user
from auth.models.models import User


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post('')
async def add_task(
    task: TaskSchemaAdd,
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
    user: User = Depends(current_active_user),    
):  
    task_id = await tasks_service.add_task(task)
    return {
        "task_id": task_id,
    }


@router.get("")
async def get_tasks(
    tasks_service: Annotated[TasksService, Depends(tasks_service)],
    user: User = Depends(current_active_user),
):
    tasks = await tasks_service.get_tasks()
    return tasks