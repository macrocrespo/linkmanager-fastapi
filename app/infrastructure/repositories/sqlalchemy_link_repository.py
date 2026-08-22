from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from app.domain.entities.link import Link, NewLink
from app.domain.entities.tag import Tag
from app.domain.repositories.link_repository import LinkRepository
from app.infrastructure.db.models.link_model import LinkModel
from app.infrastructure.db.models.tag_model import TagModel

class SqlAlchemyLinkRepository(LinkRepository):
    def __init__(self, session: AsyncSession):
        self._session = session

    def _to_entity(self, model: LinkModel) -> Link:
        return Link(
            id=model.id,
            url=model.url,
            title=model.title,
            owner_id=model.owner_id,
            tags=[Tag(
                id=t.id,
                name=t.name
            ) for t in model.tags],
            description=model.description,
        )

    async def get_by_id(self, link_id: int) -> Link | None:
        stmt = (
            select(LinkModel)
            .options(selectinload(LinkModel.tags))
            .where(LinkModel.id == link_id)
        )
        result = await self._session.execute(stmt)
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def create (self, link: NewLink) -> Link:
        tag_models = []
        for tag in link.tags:
            stmt = select(TagModel).where(TagModel.name == tag.name)
            result = await self._session.execute(stmt)
            existing = result.scalar_one_or_none()
            tag_models.append(existing or TagModel(
                name=tag.name
            ))

        model = LinkModel(
            url=link.url, 
            title=link.title, 
            owner_id=link.owner_id, 
            tags=tag_models,
            description=link.description,
        )

        self._session.add(model)
        await self._session.flush()
        await self._session.refresh(model, attribute_names=["tags"])
        return self._to_entity(model)

    async def list_by_owner(self, owner_id: int, limit: int, offset: int) -> list[Link]:
        stmt = (
            select(LinkModel)
            .options(selectinload(LinkModel.tags))
            .where(LinkModel.owner_id == owner_id)
            .limit(limit)
            .offset(offset)
        )
        result = await self._session.execute(stmt)
        return [self._to_entity(m) for m in result.scalars().all()]

    async def delete_by_owner(self, owner_id: int) -> None:
        stmt = (
            delete(LinkModel)
            .where(LinkModel.owner_id == owner_id)
        )
        await self._session.execute(stmt)