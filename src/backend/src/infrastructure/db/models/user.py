from src.infrastructure.db.options import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Uuid
import uuid


class User(Base):
	id: Mapped[Uuid] = mapped_column(primary_key=True, default=uuid.uuid5)
	username: Mapped[str]
	email: Mapped[str]
	hashed_password: Mapped[str]