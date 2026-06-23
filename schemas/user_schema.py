import uuid

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublicSchema(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    username: str
    email: EmailStr


class UserPublicListSchema(BaseModel):
    users: list[UserPublicSchema]


class UserColumn(UserSchema, UserPublicSchema):
    pass
