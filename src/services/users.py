from schemas.users import UserSchemaAdd
from repositories.base import AbstractRepository


class UserService:
    def __init__(self, user_repo: AbstractRepository):
        self.user_repo: AbstractRepository = user_repo()

    async def add_user(self, user: UserSchemaAdd) -> int:
        user_dict = user.model_dump()
        user_id = await self.user_repo.add_one(user_dict)
        print(f"task_id in services->users->add_one: {user_id}")
        return user_id
    
    async def get_users(self):
        users = await self.user_repo.find_all()
        return users
