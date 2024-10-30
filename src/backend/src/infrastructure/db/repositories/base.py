from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from src.infrastructure.db.options.db import get_async_session

from fastapi import Depends


class SQLAlchemyRepo:
    async def __call__(self):
        self._session: AsyncSession = Depends(get_async_session)
        
    @property
    async def session(self):
        return self._session
