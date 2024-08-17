from fastapi import Depends, HTTPException, status, Security
from fastapi_jwt import JwtAccessBearer, JwtAuthorizationCredentials
from src.domain.schemas.user import UserSchema


access_security = JwtAccessBearer(secret_key="very_secret_key")

def get_current_user(credentials: JwtAuthorizationCredentials = Security(access_security)):
    print('credentials:', credentials)
    return credentials.subject


def login_required(user: UserSchema = Depends(get_current_user)) -> UserSchema:
    print('user:', user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user