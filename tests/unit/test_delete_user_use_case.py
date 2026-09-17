import pytest
from app.application.use_cases.user.delete_user import DeleteUserUseCase
from app.domain.entities.user import NewUser
from app.domain.entities.link import NewLink
from app.domain.exceptions import UserNotFound
from app.domain.value_objects.role import Role
from tests.unit.fakes.fake_unit_of_work import FakeUnitOfWork

@pytest.mark.asyncio
async def test_delete_user_success():
    uow = FakeUnitOfWork()
    user = await uow.users.create(NewUser(email="test@example.com", password="hashed", role=Role.USER))
    await uow.links.create(NewLink(url="https://a.com", title="A", owner_id=user.id, tags=[]))
    use_case = DeleteUserUseCase(uow)

    await use_case.execute(user.id)

    assert await uow.users.get_by_id(user.id) is None
    assert await uow.links.list_by_owner(user.id, limit=10, offset=0) == []
    assert uow.committed is True

@pytest.mark.asyncio
async def test_delete_user_not_found_raises():
    uow = FakeUnitOfWork()
    use_case = DeleteUserUseCase(uow)

    with pytest.raises(UserNotFound):
        await use_case.execute(999)

    assert uow.committed is False
    assert uow.rolled_back is True
