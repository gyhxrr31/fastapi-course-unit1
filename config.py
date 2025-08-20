from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    DB_URL: str

    model_config = SettingsConfigDict(env_file=".env.db", extra="ignore") #игнорируем лишние переменные


class PWDSettings(BaseSettings):
    PRIVATE_KEY: str
    ALGORITHM: str

    model_config = SettingsConfigDict(env_file=".env.pwd")

dbconfig = DBSettings()
pwdconfig = PWDSettings()