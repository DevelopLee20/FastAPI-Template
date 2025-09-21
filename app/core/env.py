from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODE: str = "dev"
    CORS_ORIGINS: str = "http://localhost,http://localhost:3000,http://localhost:8080"


settings = Settings()
