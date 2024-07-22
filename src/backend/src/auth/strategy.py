from fastapi_users.authentication import JWTStrategy

from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv('auth.env'))

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=os.getenv('SECRET'), lifetime_seconds=3600)
