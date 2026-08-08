from fastapi import APIRouter, Depends
from app.application.use_cases.tag.create_tag import CreateTagUseCase
from app.application.use_cases.tag.list_tags import ListTagsUseCase
from app.di.container import get_create_tag_use_case, get_list_tags_use_case
from app.presentation.api.v1.schemas.tag_schema import TagCreateSchema, TagPublicSchema

router = APIRouter(prefix="/api/v1/tags", tags=["tags"])

@router.post("", response_model=TagPublicSchema, status_code=201)
async def create_tag(
        payload: TagCreateSchema, 
        use_case: CreateTagUseCase = Depends(get_create_tag_use_case)
    ):
    return await use_case.execute(payload.name)

@router.get("", response_model=list[TagPublicSchema])
async def list_tags(
        limit: int = 10,
        offset: int = 0,
        use_case: ListTagsUseCase = Depends(get_list_tags_use_case)
    ):
    return await use_case.execute(limit=limit, offset=offset)