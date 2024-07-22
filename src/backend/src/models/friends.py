
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db.db import Base
from sqlalchemy import ForeignKey
from uuid import UUID

# from schemas.friends import FriendSchema
class Friend(Base):
		__tablename__ = "friends"
		# subscriber_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'))
		# accepting_id: Mapped[UUID] = mapped_column(ForeignKey('user.id'))
		# is_accept: Mapped[bool]
		pon: Mapped[int]
			
	# subscriber = relationship("User", foreign_keys=[subscriber_id])
	# accepting = relationship("User", foreign_keys=[accepting_id])
    
	
	# def to_read_model(self) -> FriendSchema:
	# 		return FriendSchema(
	# 			id = self.id,
	# 			subscriber_id = self.subscriber_id,
	# 			accepting_id = self.accepting_id,
	# 			is_accept = self.is_accept
	# 		)
