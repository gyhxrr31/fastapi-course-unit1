from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import env_config


engine = create_async_engine(url=env_config.DB_URL_CONTAINER)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


