from app.domain.entities.user import NewUser, User
from app.domain.repositories.user_repository import UserRepository

class FakeUserRepository(UserRepository):

    def __init__(self):
        self._users: dict[int, User] = {}
        self._next_id = 1

    async def get_by_id(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    async def get_by_email(self, email: str) -> User | None:
        return next((u for u in self._users.values() if u.email == email), None)

    async def create(self, user: NewUser) -> User:
        result = User(id=self._next_id, email=user.email, password=user.password, role=user.role)
        self._users[result.id] = result
        self._next_id += 1
        return result

    async def list(self, limit: int, offset: int) -> list[User]:
        return list(self._users.values())[offset:offset + limit]

    async def delete(self, user_id: int) -> None:
        self._users.pop(user_id, None)
