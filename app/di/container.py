from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.infrastructure.db.session import get_db_session

from app.infrastructure.repositories.sqlalchemy_tag_repository import SqlAlchemyTagRepository
from app.application.use_cases.tag.create_tag import CreateTagUseCase
from app.application.use_cases.tag.list_tags import ListTagsUseCase

from app.infrastructure.repositories.sqlalchemy_user_repository import SqlAlchemyUserRepository
from app.application.use_cases.user.create_user import CreateUserUseCase
from app.application.use_cases.user.authenticate_user import AuthenticateUserUseCase

from app.infrastructure.repositories.sqlalchemy_link_repository import SqlAlchemyLinkRepository
from app.application.use_cases.link.create_link import CreateLinkUseCase
from app.application.use_cases.link.list_links import ListLinksUseCase

def get_create_tag_use_case(session: AsyncSession = Depends(get_db_session)) -> CreateTagUseCase:
    return CreateTagUseCase(SqlAlchemyTagRepository(session))

def get_list_tags_use_case(session: AsyncSession = Depends(get_db_session)) -> ListTagsUseCase:
    return ListTagsUseCase(SqlAlchemyTagRepository(session))

def get_create_user_use_case(session: AsyncSession = Depends(get_db_session)) -> CreateUserUseCase:
    return CreateUserUseCase(SqlAlchemyUserRepository(session))

def get_authenticate_user_use_case(session: AsyncSession = Depends(get_db_session)) -> AuthenticateUserUseCase:
    return AuthenticateUserUseCase(SqlAlchemyUserRepository(session))

def get_create_link_use_case(session: AsyncSession = Depends(get_db_session)) -> CreateLinkUseCase:
    return CreateLinkUseCase(SqlAlchemyLinkRepository(session))

def get_list_links_use_case(session: AsyncSession = Depends(get_db_session)) -> ListLinksUseCase:
    return ListLinksUseCase(SqlAlchemyLinkRepository(session))