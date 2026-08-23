from fastapi import APIRouter, Depends, status
from app.application.use_cases.user.create_user import CreateUserUseCase
from app.di.container import get_create_user_use_case
from app.presentation.api.v1.schemas.user_schema import UserCreateSchema, UserPublicSchema
from fastapi.security import OAuth2PasswordRequestForm
from app.application.use_cases.user.authenticate_user import AuthenticateUserUseCase
from app.di.container import get_authenticate_user_use_case
from app.application.use_cases.user.delete_user import DeleteUserUseCase
from app.di.container import get_delete_user_use_case
from app.presentation.api.v1.dependencies import get_current_user
from app.domain.entities.user import User

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

@router.post(
    "/register",
    response_model=UserPublicSchema,
    status_code=201,
    responses={409: {"description": "Email already registered" }},
)
async def register(payload: UserCreateSchema, use_case: CreateUserUseCase = Depends(get_create_user_use_case)):
    user = await use_case.execute(payload.email, payload.password)
    return UserPublicSchema(id=user.id, email=user.email, role=user.role.value)

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    use_case: AuthenticateUserUseCase = Depends(get_authenticate_user_use_case),
):
    token = await use_case.execute(form_data.username, form_data.password)
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_me(
    current_user: User = Depends(get_current_user),
    use_case: DeleteUserUseCase = Depends(get_delete_user_use_case),
):
    await use_case.execute(current_user.id)