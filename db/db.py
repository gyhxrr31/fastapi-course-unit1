from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker
from config import DBConfig


settings = DBConfig
engine = create_async_engine(url=settings.DB_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


