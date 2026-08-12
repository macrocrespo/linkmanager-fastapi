from pydantic import BaseModel, ConfigDict, EmailStr, field_validator

class UserCreateSchema(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def password_min_length(cls, value: str) -> str:
        if len(value) < 8:
            raise ValueError("password must be at least 8 characters long")
        return value

class UserPublicSchema(BaseModel):
    id: int
    email: str
    role: str