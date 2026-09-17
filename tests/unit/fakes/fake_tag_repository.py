from app.domain.entities.tag import NewTag, Tag
from app.domain.repositories.tag_repository import TagRepository

class FakeTagRepository(TagRepository):

    def __init__(self):
        self._tags: dict[int, Tag] = {}
        self._next_id = 1

    async def get_by_name(self, name: str) -> Tag | None:
        return next((t for t in self._tags.values() if t.name == name), None)

    async def create(self, tag: NewTag) -> Tag:
        result = Tag(id=self._next_id, name=tag.name)
        self._tags[result.id] = result
        self._next_id += 1
        return result

    async def list(self, limit: int, offset: int) -> list[Tag]:
        return list(self._tags.values())[offset:offset + limit]