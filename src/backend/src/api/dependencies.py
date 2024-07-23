from src.repositories.tasks import TasksRepository
from src.services.tasks import TasksService

from src.repositories.friends import FriendsRepository
from src.services.friends import FriendService

def tasks_service():
    return TasksService(TasksRepository)

def friend_service():
    return FriendService(FriendsRepository)