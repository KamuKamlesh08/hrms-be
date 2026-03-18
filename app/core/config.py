from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "HRMS Lite API"
    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    api_v1_prefix: str = "/api/v1"
    log_level: str = "INFO"

    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db_name: str = "hrms_lite"

    # cors_origins: str = "http://localhost:5173,http://127.0.0.1:5173,https://hrms-fe-m00t.onrender.com,"
   # just for renderer testing, as free deployment does not support to update env vars, but for local development, use the .env file
    app_cors_origins: str = (
        "http://localhost:5173,"
        "http://127.0.0.1:5173,"
        "https://hrms-fe-m00t.onrender.com"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # @property
    # def cors_origins_list(self) -> list[str]:
    #     return [item.strip() for item in self.cors_origins.split(",") if item.strip()]
    
    # just for renderer testing, as free deployment does not support to update env vars, but for local development, use the .env file
    @property
    def cors_origins_list(self) -> list[str]:
        return [item.strip() for item in self.app_cors_origins.split(",") if item.strip()]

# @lru_cache
# def get_settings() -> Settings:
#     return Settings()

# just for renderer testing, as free deployment does not support to update env vars, but for local development, use the .env file
@lru_cache
def get_settings() -> Settings:
    return Settings()