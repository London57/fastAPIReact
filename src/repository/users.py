from models.users import Users
from .base import SQLAlchemyRepository


class UsersRepository(SQLAlchemyRepository):
    model = Users

    