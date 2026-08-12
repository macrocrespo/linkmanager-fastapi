from dataclasses import dataclass
from app.domain.value_objects.role import Role

@dataclass
class NewUser:
    email: str
    password: str
    role: Role

@dataclass
class User:
    id: int
    email: str
    password: str
    role: Role