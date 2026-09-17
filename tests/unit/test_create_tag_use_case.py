import pytest
from app.application.use_cases.tag.create_tag import CreateTagUseCase
from app.domain.exceptions import TagAlreadyExists
from tests.unit.fakes.fake_tag_repository import FakeTagRepository

@pytest.mark.asyncio
async def test_create_tag_success():
    repo = FakeTagRepository()
    use_case = CreateTagUseCase(repo)

    tag = await use_case.execute("python")

    assert tag.id is not None
    assert tag.name == "python"

@pytest.mark.asyncio
async def test_create_tag_duplicate_raises():
    repo = FakeTagRepository()
    use_case = CreateTagUseCase(repo)
    await use_case.execute("python")

    with pytest.raises(TagAlreadyExists):
        await use_case.execute("python")