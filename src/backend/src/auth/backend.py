from fastapi_users.authentication import AuthenticationBackend

from .transport import bearer_transport
from .strategy import get_jwt_strategy


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
