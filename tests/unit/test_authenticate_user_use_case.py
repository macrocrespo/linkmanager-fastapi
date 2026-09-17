import pytest
from app.application.use_cases.user.authenticate_user import AuthenticateUserUseCase
from app.domain.entities.user import NewUser
from app.domain.exceptions import InvalidCredentials
from app.domain.value_objects.role import Role
from app.core.security import hash_password
from tests.unit.fakes.fake_user_repository import FakeUserRepository

@pytest.mark.asyncio
async def test_authenticate_success():
    repo = FakeUserRepository()
    await repo.create(NewUser(email="test@example.com", password=hash_password("secret123"), role=Role.USER))
    use_case = AuthenticateUserUseCase(repo)

    token = await use_case.execute("test@example.com", "secret123")

    assert isinstance(token, str)

@pytest.mark.asyncio
async def test_authenticate_wrong_password_raises():
    repo = FakeUserRepository()
    await repo.create(NewUser(email="test@example.com", password=hash_password("secret123"), role=Role.USER))
    use_case = AuthenticateUserUseCase(repo)

    with pytest.raises(InvalidCredentials):
        await use_case.execute("test@example.com", "wrong-pass")

@pytest.mark.asyncio
async def test_authenticate_unknown_email_raises():
    repo = FakeUserRepository()
    use_case = AuthenticateUserUseCase(repo)

    with pytest.raises(InvalidCredentials):
        await use_case.execute("nobody@example.com", "secret123")
