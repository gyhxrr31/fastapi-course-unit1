from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    DB_URL: str

    model_config = SettingsConfigDict(env_file=".env.db", extra="ignore") #игнорируем лишние переменные


DBConfig = DBSettings()