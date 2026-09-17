import pytest
from app.application.use_cases.tag.list_tags import ListTagsUseCase
from app.domain.entities.tag import NewTag
from tests.unit.fakes.fake_tag_repository import FakeTagRepository

@pytest.mark.asyncio
async def test_list_tags_returns_paginated():
    repo = FakeTagRepository()
    for name in ("python", "fastapi", "docker"):
        await repo.create(NewTag(name=name))
    use_case = ListTagsUseCase(repo)

    result = await use_case.execute(limit=2, offset=1)

    assert [t.name for t in result] == ["fastapi", "docker"]
