from app.domain.repositories.unit_of_work import UnitOfWork
from tests.unit.fakes.fake_user_repository import FakeUserRepository
from tests.unit.fakes.fake_link_repository import FakeLinkRepository

class FakeUnitOfWork(UnitOfWork):

    def __init__(self):
        self.users = FakeUserRepository()
        self.links = FakeLinkRepository()
        self.committed = False
        self.rolled_back = False

    async def commit(self) -> None:
        self.committed = True

    async def rollback(self) -> None:
        self.rolled_back = True
