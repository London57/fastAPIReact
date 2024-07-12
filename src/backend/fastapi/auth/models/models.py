from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import Mapped
from db.db import Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    username: Mapped[str]





