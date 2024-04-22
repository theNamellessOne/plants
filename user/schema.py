from pydantic import BaseModel, EmailStr

from common.schema import OrmBase


class UserRead(OrmBase):
    id: int
    is_admin: bool
    username: str
    email: EmailStr


class UserBase(BaseModel):
    email: EmailStr
    password: str


class UserLogin(UserBase):
    pass


class UserRegister(UserBase):
    username: str


class UserUpdate(UserRegister):
    pass
