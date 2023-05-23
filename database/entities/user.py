from typing import Optional
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):

    __tablename__ = 'users'

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(
        max_length=100,
    )
    surname: str = Field(
        max_length=100,
    )
    login: str = Field(
        max_length=100,
    )
    password: str = Field(
        max_length=100,
    )
    admin: bool = Field(
        default=0
    )
