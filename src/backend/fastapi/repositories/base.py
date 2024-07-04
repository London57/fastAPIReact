from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    

class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict):
        async with async_session_maker() as session:
            statement = insert(self.model)\
                    .values(**data)
            res = await session.execute(statement)
            await session.commit()
            print('res in repo->add_one')
            return res.lastrowid
        
    async def find_all(self):
        async with async_session_maker() as session:
            statement = select(self.model)
            res = await session.execute(statement)
            res = [row[0].to_read_model() for row in res.all()]
            print(f"res in repo->find_all: {res}")
            return res