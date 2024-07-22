from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped
from src.db.db import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    username: Mapped[str]