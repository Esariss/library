from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "library"
    debug: bool = True
    database_url: str = "sqlite:///./library.db"

    cors_origins: list[str] = [
        "http://localhost:8000",
        "http://127.0.0.1:8000"
    ]

    static_dir: str = "static"
    pdf_dir: str = "static/pdf"

    model_config = SettingsConfigDict(env_file=".env")

setting = Settings()