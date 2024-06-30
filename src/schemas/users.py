from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str

class UserSchemaAdd(BaseModel):
    name: str