from app.domain.entities.user import NewUser, User
from app.domain.exceptions import UserAlreadyExists
from app.domain.repositories.user_repository import UserRepository
from app.domain.value_objects.role import Role
from app.core.security import hash_password

class CreateUserUseCase:
    def __init__(self, user_repo: UserRepository) -> None:
        self._user_repo = user_repo

    async def execute(self, email: str, plain_password: str) -> User:
        existing = await self._user_repo.get_by_email(email)
        if existing:
            raise UserAlreadyExists(f"Email {email} already registered")

        new_user = NewUser(
            email=email, 
            password=hash_password(plain_password),
            role=Role.USER
        )
        return await self._user_repo.create(new_user)