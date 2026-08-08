from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.session import get_db_session
from app.infrastructure.repositories.sqlalchemy_tag_repository import SqlAlchemyTagRepository
from app.application.use_cases.tag.create_tag import CreateTagUseCase
from app.application.use_cases.tag.list_tags import ListTagsUseCase

def get_create_tag_use_case(session: AsyncSession = Depends(get_db_session)) -> CreateTagUseCase:
    return CreateTagUseCase(SqlAlchemyTagRepository(session))

def get_list_tags_use_case(session: AsyncSession = Depends(get_db_session)) -> ListTagsUseCase:
    return ListTagsUseCase(SqlAlchemyTagRepository(session))