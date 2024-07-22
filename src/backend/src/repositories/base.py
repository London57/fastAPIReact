from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from src.db.db import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError
    
    @abstractmethod
    async def get_with_filter_where():
        return NotImplementedError

def data_to_where(data: dict):
	l = []
	items = list(data.items())

	for i, j in items:
		if i != items[-1][0]:
			l.append(f'{i} = {j} and ')
		else: 
			l.append(f'{i} = {j}')
	return ''.join(l)

print('in repo')

class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict):
        async with async_session_maker() as session:
            statement = insert(self.model)\
                    .values(**data)
            res = await session.execute(statement)
            a = await session.flush()
            print(a, 'fffffffffffffffffffffffff')
            print('res in repo->add_one')
            return res.lastrowid
        
    async def find_all(self):
        async with async_session_maker() as session:
            statement = select(self.model)
            res = await session.execute(statement)
            res = [row[0].to_read_model() for row in res.all()]
            print(f"res in repo->find_all: {res}")
            return res
    
    async def get_with_filter_where(self, data: dict):
        async with async_session_maker() as session:
            statement = select(self.model).where(data_to_where(data))
            res = await session.execute(statement)
            a = session.flush(res)
            print(a)
            