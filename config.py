from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    DB_URL: str
    PRIVATE_KEY: str
    ALGORITHM: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore") #игнорируем лишние переменные


env_config = EnvConfig()
