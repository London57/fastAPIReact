import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from db.db import create_tables, drop_tables
from api.routers import all_routers

from auth.users import fastapiUsers
from auth.schemas import CreateUserSchema, ReadUserSchema


@asynccontextmanager
async def lifespan(app):
    await create_tables()
    yield
    import sys
    sys.exit()


app = FastAPI(
    lifespan=lifespan
)

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials =True,
    allow_methods=['GET', 'POST'], 
    allow_headers=['Access-Control-Allow-Origin', 'Access-Control-Allow-Headers'],
)

for router in all_routers:
    app.include_router(router)

app.include_router(
    fastapiUsers.get_register_router(ReadUserSchema, CreateUserSchema), # first param: response_model
    prefix='/auth',
    tags=['Auuth'],
)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=8080)