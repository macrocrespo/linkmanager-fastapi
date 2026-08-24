from abc import ABC, abstractmethod
from app.domain.entities.link import Link
from app.domain.repositories.link_repository import LinkRepository

class LinkFilterStrategy(ABC):
    @abstractmethod
    async def apply(
        self, 
        repo: LinkRepository, 
        owner_id: int, 
        limit: int, 
        offset: int
    ) -> list[Link]: ...