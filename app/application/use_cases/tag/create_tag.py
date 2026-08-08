from app.domain.entities.tag import NewTag, Tag
from app.domain.repositories.tag_repository import TagRepository

class CreateTagUseCase:

    def __init__(self, tag_repo: TagRepository):
        self._tag_repo = tag_repo

    async def execute(self, name: str) -> Tag:
        return await self._tag_repo.create(NewTag(name=name))