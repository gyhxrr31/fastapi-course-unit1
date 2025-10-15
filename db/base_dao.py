from db.db import async_session_maker
from sqlalchemy import select, insert


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            statement = select(cls.model).filter_by(id=model_id)
            result = await session.execute(statement)
        return result.scalars().one_or_none()


    @classmethod
    async def get_one_or_none(cls, **value):
        async with async_session_maker() as session:
            statement = select(cls.model).filter_by(**value)
            result = await session.execute(statement)
        return result.scalars().one_or_none()


    @classmethod
    async def select_all(cls, **value):
        async with async_session_maker() as session:
            statement = select(cls.model).filter_by(**value)
            result = await session.execute(statement)
        return result.scalars().all()


    @classmethod
    async def insert_one(cls, **value):
        async with async_session_maker() as session:
            statement = insert(cls.model).values(**value)
            await session.execute(statement)
            await session.commit()


    @classmethod
    async def add_many(cls, **data):
        async with async_session_maker() as session:
            statement = cls.model(**data)
            session.add(statement)
            await session.commit()
            return statement


    @classmethod
    async def delete(cls, model_id: int):
        async with async_session_maker() as session:
            instance = await cls.find_by_id(model_id)
            if instance:
                await session.delete(instance)
                await session.commit()
            return instance