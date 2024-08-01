from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.options.db import async_session_maker


class SQLAlchemyRepo:
    def __init__(self, session: AsyncSession):
        self._session: AsyncSession = session

    @property
    def session(self):
        return self._session