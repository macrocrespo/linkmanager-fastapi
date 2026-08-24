from app.domain.entities.link import Link
from app.domain.repositories.link_repository import LinkRepository
from app.application.strategies.link_filter.base import LinkFilterStrategy

class ListLinksUseCase:
    def __init__(self, link_repo: LinkRepository):
        self._link_repo = link_repo

    async def execute(self, owner_id: int, strategy: LinkFilterStrategy, limit: int, offset: int) -> list[Link]:
        return await strategy.apply(self._link_repo, owner_id, limit, offset)