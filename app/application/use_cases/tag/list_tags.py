from app.domain.entities.tag import Tag
from app.domain.repositories.tag_repository import TagRepository

class ListTagsUseCase:
    
    def __init__(self, tag_repo: TagRepository):
        self._tag_repo = tag_repo

    async def execute(self, limit: int, offset: int) -> list[Tag]:
        return await self._tag_repo.list(limit, offset)