from fastapi import APIRouter, Depends
from app.application.use_cases.user.create_user import CreateUserUseCase
from app.di.container import get_create_user_use_case
from app.presentation.api.v1.schemas.user_schema import UserCreateSchema, UserPublicSchema

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