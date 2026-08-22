from app.domain.entities.link import Link, NewLink
from app.domain.entities.tag import NewTag
from app.domain.repositories.link_repository import LinkRepository

class CreateLinkUseCase:
    def __init__(self, link_repo: LinkRepository):
        self._link_repo = link_repo

    async def execute(
        self, 
        url: str, 
        title: str, 
        owner_id: int, 
        tag_names: list[str], 
        description: str | None = None
    ) -> Link:
        new_link = NewLink(
            url=url, 
            title=title, 
            owner_id=owner_id, 
            tags=[NewTag(name=n) for n in tag_names],
            description=description,
        )
        return await self._link_repo.create(new_link)