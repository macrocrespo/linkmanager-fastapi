from app.domain.entities.link import Link, NewLink
from app.domain.entities.tag import Tag
from app.domain.repositories.link_repository import LinkRepository

class FakeLinkRepository(LinkRepository):

    def __init__(self):
        self._links: dict[int, Link] = {}
        self._next_id = 1

    async def get_by_id(self, link_id: int) -> Link | None:
        return self._links.get(link_id)

    async def create(self, link: NewLink) -> Link:
        tags = [Tag(id=i + 1, name=t.name) for i, t in enumerate(link.tags)]
        result = Link(
            id=self._next_id,
            url=link.url,
            title=link.title,
            owner_id=link.owner_id,
            tags=tags,
            description=link.description,
        )
        self._links[result.id] = result
        self._next_id += 1
        return result

    async def list_by_owner(self, owner_id: int, limit: int, offset: int) -> list[Link]:
        owned = [l for l in self._links.values() if l.owner_id == owner_id]
        return owned[offset:offset + limit]

    async def delete_by_owner(self, owner_id: int) -> None:
        for link_id in [l.id for l in self._links.values() if l.owner_id == owner_id]:
            del self._links[link_id]

    async def list_by_tag(self, owner_id: int, tag_name: str, limit: int, offset: int) -> list[Link]:
        matching = [
            l for l in self._links.values()
            if l.owner_id == owner_id and tag_name in [t.name for t in l.tags]
        ]
        return matching[offset:offset + limit]
