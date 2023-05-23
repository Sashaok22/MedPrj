from datetime import date
from typing import Optional
from sqlmodel import Field, SQLModel

class Patient(SQLModel, table=True):

    __tablename__ = 'patients'

    id: Optional[int] = Field(primary_key=True, default=None)
    name: str = Field(
        max_length=100,
    )
    surname: str = Field(
        max_length=100,
    )
    patronymic: str = Field(
        max_length=100,
    )
    date_of_birth: date = Field(
    )
    polis: str = Field(
        max_length=100,
    )

