from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.user import NewUser, User
from app.domain.repositories.user_repository import UserRepository
from app.domain.value_objects.role import Role
from app.infrastructure.db.models.user_model import UserModel

class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    def _to_entity(self, model: UserModel) -> User:
        return User(id=model.id, email=model.email, password=model.password, role=Role(model.role))

    async def get_by_id(self, user_id: int) -> User | None:
        model = await self._session.get(UserModel, user_id)
        return self._to_entity(model) if model else None

    async def get_by_email(self, email: str) -> User | None:
        result = await self._session.execute(select(UserModel).where(UserModel.email == email))
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def create(self, user: NewUser) -> User:
        model = UserModel(email=user.email, password=user.password, role=user.role.value)
        self._session.add(model)
        await self._session.flush()
        await self._session.refresh(model)
        return self._to_entity(model)

    async def list(self, limit: int, offset: int) -> list[User]:
        result = await self._session.execute(select(UserModel).limit(limit).offset(offset))
        return [self._to_entity(m) for m in result.scalars().all()]

    async def delete(self, user_id: int) -> None:
        await self._session.execute(delete(UserModel).where(UserModel.id == user_id))