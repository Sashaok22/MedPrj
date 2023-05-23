from datetime import date
from typing import Optional
from sqlalchemy import Column, ForeignKey, Integer
from sqlmodel import Field, SQLModel

class Diagnosis(SQLModel, table=True):

    __tablename__ = 'diagnosis'

    id: Optional[int] = Field(primary_key=True, default=None)
    user_id: Optional[int] = Field(
        sa_column=Column(Integer, ForeignKey(column='users.id', ondelete='SET NULL')),
    )
    patient_id: Optional[int] = Field(
        sa_column=Column(Integer, ForeignKey(column='patients.id', ondelete='SET NULL')),
    )
    result: str = Field(
        max_length=100,
    )
    description: str = Field(
        max_length=255,
    )
    diagnosis_date: date = Field(
    )
    system_confidence: str = Field(
        max_length=100,
    )

