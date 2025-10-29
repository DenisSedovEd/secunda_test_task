from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str
    api_key: str

    class Config:
        env_file = ".env"


settings = Settings()

# BASE_DIR = Path(__file__).resolve().parent
#
# DB_URL = f"postgresql+asyncpg://app:password@localhost:5432/app_db"
# DB_ECHO = True
