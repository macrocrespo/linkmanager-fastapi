from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import decode_access_token
from app.domain.entities.user import User
from app.domain.value_objects.role import Role
from app.infrastructure.db.session import get_db_session
from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_db_session),
) -> User:

    user_id = decode_access_token(token)
    if user_id is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

    user = await SqlAlchemyUserRepository(session).get_by_id(int(user_id))
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user

def require_role(required_role: Role):
    async def checker(current_user: User = Depends(get_current_user)) -> User:
        if current_user.role != required_role:
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
        return current_user
    return checker