from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.session import get_db_session
from app.infrastructure.db.models.tag_model import TagModel
from app.presentation.api.v1.schemas.tag_schema import TagCreateSchema, TagPublicSchema

router = APIRouter(prefix="/api/v1/tags", tags=["tags"])

@router.post("", response_model=TagPublicSchema, status_code=201)
async def create_tag(payload: TagCreateSchema, session: AsyncSession = Depends(get_db_session)):
    model = TagModel(name=payload.name)
    session.add(model)
    await session.flush()
    await session.refresh(model)
    return model

@router.get("", response_model=list[TagPublicSchema])
async def list_tags(session: AsyncSession = Depends(get_db_session)):
    result = await session.execute(select(TagModel))
    return result.scalars().all()