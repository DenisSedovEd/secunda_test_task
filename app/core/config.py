from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

DB_URL = f"postgresql+asyncpg://app:password@localhost:5432/app_db"
DB_ECHO = True
