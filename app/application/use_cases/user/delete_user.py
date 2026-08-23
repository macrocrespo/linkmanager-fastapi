from app.domain.exceptions import UserNotFound
from app.domain.repositories.unit_of_work import UnitOfWork

class DeleteUserUseCase:

    def __init__(self, uow: UnitOfWork):
        self._uow = uow

    async def execute(self, user_id: int) -> None:
        async with self._uow:
            user = await self._uow.users.get_by_id(user_id)
            if user is None:
                raise UserNotFound(f"User {user_id} not found")

            await self._uow.links.delete_by_owner(user_id)
            await self._uow.users.delete(user_id)