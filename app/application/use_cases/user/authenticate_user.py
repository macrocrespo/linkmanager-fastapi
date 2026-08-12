from app.domain.exceptions import InvalidCredentials
from app.domain.repositories.user_repository import UserRepository
from app.core.security import verify_password, create_access_token

class AuthenticateUserUseCase:
    def __init__(self, user_repo: UserRepository):
        self._user_repo = user_repo

    async def execute(self, email: str, plain_password: str) -> str:
        user = await self._user_repo.get_by_email(email)
        if not user or not verify_password(plain_password, user.password):
            raise InvalidCredentials("Invalid credentials")
        return create_access_token(subject=str(user.id))