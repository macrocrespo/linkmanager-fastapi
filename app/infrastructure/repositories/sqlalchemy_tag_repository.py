from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.domain.entities.tag import NewTag, Tag
from app.domain.repositories.tag_repository import TagRepository
from app.infrastructure.db.models.tag_model import TagModel

class SqlAlchemyTagRepository(TagRepository):

    def __init__(self, session: AsyncSession):
        self._session = session

    def _to_entity(self, model: TagModel) -> Tag:
        return Tag(id=model.id, name=model.name)

    async def get_by_name(self, name: str) -> Tag | None:
        result = await self._session.execute(select(TagModel).where(TagModel.name == name))
        model = result.scalar_one_or_none()
        return self._to_entity(model) if model else None

    async def create(self, tag: NewTag) -> Tag:
        model = TagModel(name=tag.name)
        self._session.add(model)
        await self._session.flush()
        await self._session.refresh(model)
        return self._to_entity(model)

    async def list(self, limit: int, offset: int) -> list[Tag]:
        result = await self._session.execute(select(TagModel).limit(limit).offset(offset))
        return [self._to_entity(m) for m in result.scalars().all()]