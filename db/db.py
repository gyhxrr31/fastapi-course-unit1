from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import dbconfig


engine = create_async_engine(url=dbconfig.DB_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


