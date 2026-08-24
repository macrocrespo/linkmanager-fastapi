from app.application.strategies.link_filter.base import LinkFilterStrategy

class ByTagStrategy(LinkFilterStrategy):
    def __init__(self, tag_name: str):
        self._tag_name = tag_name

    async def apply(self, repo, owner_id, limit, offset):
        return await repo.list_by_tag(owner_id, self._tag_name, limit, offset)