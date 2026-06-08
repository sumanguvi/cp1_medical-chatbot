"""Application settings."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration class."""

    PROJECT_NAME: str
    API_V1_STR: str
    DEBUG: bool
    LOG_LEVEL: str

    EMBEDDING_MODEL: str

    VECTOR_DB_PATH: str

    DATABASE_URL: str

    class Config:
        env_file = '.env'


settings = Settings()
