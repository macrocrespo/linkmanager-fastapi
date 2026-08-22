from abc import ABC, abstractmethod
from app.domain.entities.link import Link, NewLink

class LinkRepository(ABC):
    @abstractmethod
    async def get_by_id(self, link_id: int) -> Link | None: ...

    @abstractmethod
    async def create(self, link: NewLink) -> Link: ...

    @abstractmethod
    async def list_by_owner(self, owner_id: int, limit: int, offset: int) -> list[Link]: ...

    @abstractmethod
    async def delete_by_owner(self, owner_id: int) -> None: ...