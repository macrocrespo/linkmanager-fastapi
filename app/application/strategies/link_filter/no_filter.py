from app.application.strategies.link_filter.base import LinkFilterStrategy

class NoFilterStrategy(LinkFilterStrategy):
    async def apply(self, repo, owner_id, limit, offset):
        return await repo.list_by_owner(owner_id, limit, offset)