import pytest
from app.application.use_cases.user.create_user import CreateUserUseCase
from app.domain.exceptions import UserAlreadyExists
from app.domain.value_objects.role import Role
from tests.unit.fakes.fake_user_repository import FakeUserRepository

@pytest.mark.asyncio
async def test_create_user_success():
    repo = FakeUserRepository()
    use_case = CreateUserUseCase(repo)

    user = await use_case.execute("test@example.com", "secret123")

    assert user.id is not None
    assert user.password != "secret123"
    assert user.role == Role.USER

@pytest.mark.asyncio
async def test_create_user_duplicate_raises():
    repo = FakeUserRepository()
    use_case = CreateUserUseCase(repo)
    await use_case.execute("test@example.com", "secret123")

    with pytest.raises(UserAlreadyExists):
        await use_case.execute("test@example.com", "other-pass")
