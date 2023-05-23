from typing import Optional
from sqlalchemy import Column, ForeignKey, Integer
from sqlmodel import Field, SQLModel

class ImgData(SQLModel, table=True):

    __tablename__ = 'img_data'

    id: Optional[int] = Field(primary_key=True, default=None)
    diagnosis_id: Optional[int] = Field(
        sa_column=Column(Integer, ForeignKey(column='diagnosis.id', ondelete='SET NULL')),
    )
    img: bytes
