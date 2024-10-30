from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from uuid import UUID

from src.infrastructure.db.options.db import Base
from src.domain.schemas.friends import FriendSchema


class Friend(Base):
		__tablename__ = "friends"
		subscriber_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
		accepting_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
		is_accept: Mapped[bool]
			
		def to_read_model(self) -> FriendSchema:
			return FriendSchema(
				id = self.id,
				subscriber_id = self.subscriber_id,
				accepting_id = self.accepting_id,
				is_accept = self.is_accept
			)
