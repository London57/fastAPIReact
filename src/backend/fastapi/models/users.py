from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.users import UserSchema


class Users(Base):
    __tablename__ = "users"


    name: Mapped[str]
    
    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
        )