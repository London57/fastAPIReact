from pydantic import BaseModel, field_validator


class Username(BaseModel):
	text: str

	@field_validator("text")
	def validate_username(username):
		if not len(username) > 5:
			raise ValueError("username length must be more than 5 characters")
		return username