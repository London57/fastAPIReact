from pydantic import BaseModel
from uuid import UUID


class FriendSchema(BaseModel):
	id: UUID
	subscriber_id: UUID
	accepting_id: UUID
	is_accept: bool

class FriendSchemaAdd(BaseModel):
	subscriber_id: UUID
	accepting_id: UUID

