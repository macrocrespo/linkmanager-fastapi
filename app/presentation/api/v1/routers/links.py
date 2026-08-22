from fastapi import APIRouter, Depends
from app.application.use_cases.link.create_link import CreateLinkUseCase
from app.application.use_cases.link.list_links import ListLinksUseCase
from app.di.container import get_create_link_use_case, get_list_links_use_case
from app.presentation.api.v1.schemas.link_schema import LinkCreateSchema, LinkPublicSchema
from app.presentation.api.v1.dependencies import get_current_user
from app.domain.entities.user import User

router = APIRouter(prefix="/api/v1/links", tags=["links"])

def _to_public(link) -> LinkPublicSchema:
    return LinkPublicSchema(
        id=link.id, 
        url=link.url, 
        title=link.title, 
        tags=[t.name for t in link.tags],
        description=link.description,
    )

@router.post("", response_model=LinkPublicSchema, status_code=201)
async def create_link(
    payload: LinkCreateSchema,
    current_user: User = Depends(get_current_user),
    use_case: CreateLinkUseCase = Depends(get_create_link_use_case),
):
    link = await use_case.execute(
        str(payload.url),
        payload.title, 
        current_user.id, 
        payload.tags, 
        payload.description
    )
    return _to_public(link)

@router.get("", response_model=list[LinkPublicSchema])
async def list_links(
    current_user: User = Depends(get_current_user),
    use_case: ListLinksUseCase = Depends(get_list_links_use_case),
):
    links = await use_case.execute(
        current_user.id,
        limit=20,
        offset=0
    )
    return [_to_public(link) for link in links]