from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlmodel import SQLModel
import tkinter as tk
import database
from ui.ui import Authorization


class Settings:
    db = database.Settings()


class DB:
    engine = create_engine(Settings.db.DATABASE_URL)

    session = sessionmaker(bind=engine)

    if not database_exists(engine.url):
        create_database(engine.url)
        SQLModel.metadata.create_all(engine)





if __name__ == "__main__":
    aut = tk.Tk()
    aut2 = Authorization(aut, DB.session())
    aut2.pack()
    aut.title("Авторизация")
    aut.geometry("700x400+10+50")
    aut.resizable(False, False)
    aut.mainloop()
