import uvicorn
from  fastapi import FastAPI

from contextlib import asynccontextmanager
from db.db import create_tables, drop_tables
from api.routers import all_routers



@asynccontextmanager
async def lifespan(app):
    await create_tables()
    yield
    await drop_tables()


app = FastAPI(
    title='аналог Asana',
    lifespan=lifespan
)

for router in all_routers:
    app.include_router(router)




if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)