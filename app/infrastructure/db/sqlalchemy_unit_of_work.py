from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.repositories.unit_of_work import UnitOfWork
from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from app.infrastructure.repositories.sqlalchemy_link_repository import SqlAlchemyLinkRepository

class SqlAlchemyUnitOfWork(UnitOfWork):

    def __init__(self, session: AsyncSession):
        self._session = session
        self.users = SqlAlchemyUserRepository(session)
        self.links = SqlAlchemyLinkRepository(session)

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()