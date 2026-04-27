from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Analytics Dashboard API"
    jwt_secret: str = "change-me"
    log_level: str = "INFO"

settings = Settings()
