from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_NAME: str = 'maths_model'
    DATABASE_HOST: str = 'localhost'
    DATABASE_PORT: int = 3306
    DATABASE_USER: str = 'admin'
    DATABASE_PASS: str = 'admin'

    ALEMBIC_SCRIPT_LOCATION: str = 'database:alembic'

    ALEMBIC_VERSION_LOCATIONS: str = 'database:migrations'

    ALEMBIC_MIGRATION_FILENAME_TEMPLATE: str = (
        '%%(year)d_'
        '%%(month).2d_'
        '%%(day).2d_'
        '%%(hour).2d_'
        '%%(minute).2d_'
        '%%(second).2d_'
        '%%(slug)s'
    )

    @property
    def DATABASE_URL(self):
        url = 'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

        return url.format(
            db_user=self.DATABASE_USER,
            db_pass=self.DATABASE_PASS,
            db_host=self.DATABASE_HOST,
            db_name=self.DATABASE_NAME,
            db_port=self.DATABASE_PORT,
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
