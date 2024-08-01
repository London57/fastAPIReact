from pydantic import BaseModel, field_validator

import re


class Email(BaseModel):
	address: str

	@field_validator("address")
	@staticmethod
	def validate_email(email):
		if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
			raise ValueError("invalid email")
		return email