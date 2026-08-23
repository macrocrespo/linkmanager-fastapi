from abc import ABC, abstractmethod
from app.domain.repositories.user_repository import UserRepository
from app.domain.repositories.link_repository import LinkRepository

class UnitOfWork(ABC):

    users: UserRepository
    links: LinkRepository

    async def __aenter__(self) -> "UnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()

    @abstractmethod
    async def commit(self) -> None: ...

    @abstractmethod
    async def rollback(self) -> None: ...