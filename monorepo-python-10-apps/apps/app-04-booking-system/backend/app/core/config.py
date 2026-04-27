from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Booking System API"
    jwt_secret: str = "change-me"
    log_level: str = "INFO"

settings = Settings()
