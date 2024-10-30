from src.infrastructure.db.options import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Uuid
from uuid import UUID, uuid4

class User(Base):
	__tablename__ = 'users'

	id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
	username: Mapped[str]
	email: Mapped[str]
	hashed_password: Mapped[str]