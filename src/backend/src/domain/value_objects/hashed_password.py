from pydantic import BaseModel, field_serializer
from passlib import hash


class Hashed_password(BaseModel):
	text: str

	@field_serializer('text')
	@staticmethod
	def hash_password(password):
		return hash.argon2.hash(password)