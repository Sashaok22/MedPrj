from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlmodel import SQLModel

import database


class Settings:
    db = database.Settings()


class DB:
    engine = create_engine(Settings.db.DATABASE_URL)

    context = sessionmaker(bind=engine)
    if not database_exists(engine.url):
        create_database(engine.url)
    SQLModel.metadata.create_all(engine)



if __name__ == 'main':
    db = DB.context
