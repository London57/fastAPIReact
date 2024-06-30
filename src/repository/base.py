from abc import ABC, abstractmethod

from sqlalchemy import insert, select

from db.db import async_session_maker, Base


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    

class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            statement = insert(self.model)\
                    .values(**data)\
                    .returning(self.model.id)
            res = await session.execute(statement)
            await session.commit()
            return res
        
    async def find_all(self):
        async with async_session_maker() as session:
            statement = select(self.model)
            res = await session.execute(statement)
            print(f"res in rep->base: {res}")
            res = [row[0].to_read_model() for row in res.all()]
            return res