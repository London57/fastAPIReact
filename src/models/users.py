from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    