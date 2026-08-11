from app.domain.entities.tag import NewTag, Tag
from app.domain.exceptions import TagAlreadyExists
from app.domain.repositories.tag_repository import TagRepository

class CreateTagUseCase:

    def __init__(self, tag_repo: TagRepository):
        self._tag_repo = tag_repo

    async def execute(self, name: str) -> Tag:
        existing = await self._tag_repo.get_by_name(name)
        if existing:
            raise TagAlreadyExists(f"Tag '{name}' already exists.")
        return await self._tag_repo.create(NewTag(name=name))