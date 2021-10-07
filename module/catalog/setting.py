from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding='utf-8', case_sensitive=False, env_file='module/catalog/.env'
    )

    database_url: str
