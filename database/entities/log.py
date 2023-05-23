from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, ForeignKey, Integer

class Log(SQLModel, table=True):

    __tablename__ = 'logs'

    id: Optional[int] = Field(primary_key=True, default=None)
    user_id: Optional[int] = Field(
        sa_column=Column(Integer, ForeignKey(column='users.id', ondelete='SET NULL')),
    )
    date: date
