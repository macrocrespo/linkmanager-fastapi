import pytest
from app.application.use_cases.link.list_links import ListLinksUseCase
from app.application.strategies.link_filter.no_filter import NoFilterStrategy
from app.application.strategies.link_filter.by_tag import ByTagStrategy
from app.domain.entities.link import NewLink
from app.domain.entities.tag import NewTag
from tests.unit.fakes.fake_link_repository import FakeLinkRepository

@pytest.mark.asyncio
async def test_list_links_no_filter_strategy():
    repo = FakeLinkRepository()
    await repo.create(NewLink(url="https://a.com", title="A", owner_id=1, tags=[]))
    await repo.create(NewLink(url="https://b.com", title="B", owner_id=2, tags=[]))
    use_case = ListLinksUseCase(repo)

    result = await use_case.execute(owner_id=1, strategy=NoFilterStrategy(), limit=10, offset=0)

    assert [l.url for l in result] == ["https://a.com"]

@pytest.mark.asyncio
async def test_list_links_by_tag_strategy():
    repo = FakeLinkRepository()
    await repo.create(NewLink(url="https://a.com", title="A", owner_id=1, tags=[NewTag(name="python")]))
    await repo.create(NewLink(url="https://b.com", title="B", owner_id=1, tags=[NewTag(name="docker")]))
    use_case = ListLinksUseCase(repo)

    result = await use_case.execute(owner_id=1, strategy=ByTagStrategy("python"), limit=10, offset=0)

    assert [l.url for l in result] == ["https://a.com"]
