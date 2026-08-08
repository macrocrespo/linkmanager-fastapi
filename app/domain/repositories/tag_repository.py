from abc import ABC, abstractmethod
from app.domain.entities.tag import NewTag, Tag

class TagRepository(ABC):

    @abstractmethod
    async def get_by_name(self, name: str) -> Tag | None: ...

    @abstractmethod
    async def create(self, tag: NewTag) -> Tag: ...

    @abstractmethod
    async def list(self, limit: int, offset: int) -> list[Tag]: ...
