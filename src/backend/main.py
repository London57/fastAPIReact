import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


from src.infrastructure.db.options.create_tables import create_tables
from src.presentation.api.routers import all_routers

from src.auth.backend import auth_backend
from src.auth.schemas import CreateUserSchema, ReadUserSchema
from src.auth.users import fastapiUsers

from fastapi.security import OAuth2PasswordRequestForm

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
    allow_methods=['*'], 
    # allow_headers=['Access-Control-Allow-Origin', 'Access-Control-Allow-Headers', 'Cookie', 'Authorization'],
    allow_headers=['*'],
)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True, port=8000)



