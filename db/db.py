from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import env_config


if env_config.MODE == "TEST":
    DB_URL = env_config.TEST_DB_URL
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DB_URL = env_config.DB_URL_LOCAL
    DATABASE_PARAMS = None


engine = create_async_engine(DB_URL, **DATABASE_PARAMS)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


