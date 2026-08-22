from app.domain.entities.link import Link
from app.domain.repositories.link_repository import LinkRepository

class ListLinksUseCase:
    def __init__(self, link_repo: LinkRepository):
        self._link_repo = link_repo

    async def execute(self, owner_id: int, limit: int, offset: int) -> list[Link]:
        return await self._link_repo.list_by_owner(owner_id, limit, offset)