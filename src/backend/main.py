import sys, os

# if __name__ == '__main__':
#     sys.path.append()
print(sys.path)

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


from src.db.create_tables import create_tables
from src.api.routers import all_routers

from src.auth.backend import auth_backend
from src.auth.schemas import CreateUserSchema, ReadUserSchema
from src.auth.users import fastapiUsers


@asynccontextmanager
async def lifespan(app):
    await create_tables()
    yield

app = FastAPI(
    lifespan=lifespan
)

for router in all_routers:
    app.include_router(router)

app.include_router(
    fastapiUsers.get_register_router(ReadUserSchema, CreateUserSchema), # first param: response_model
    prefix='/auth',
    tags=['Registration'],
)

app.include_router(
    fastapiUsers.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Authentication"],
)

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['GET', 'POST'], 
    allow_headers=['Access-Control-Allow-Origin', 'Access-Control-Allow-Headers'],
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=8000)



