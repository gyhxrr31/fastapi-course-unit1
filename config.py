from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    DB_URL_CONTAINER: str
    DB_URL_LOCAL: str
    PRIVATE_KEY: str
    ALGORITHM: str
    ORIGINS: list
    REDIS_URL: str
    SMTP_HOST: str
    SMTP_PORT: str
    SMTP_USER: str
    SMTP_PWD: str
    model_config = SettingsConfigDict(env_file=".env", extra="ignore") #игнорируем лишние переменные


env_config = EnvConfig()
