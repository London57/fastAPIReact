from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    titile: Mapped[str]
    author_id:  Mapped[int] = mapped_column(ForeignKey("users.id"))
    assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    