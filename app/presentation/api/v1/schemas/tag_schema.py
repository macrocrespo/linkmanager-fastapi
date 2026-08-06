from pydantic import BaseModel

class TagCreateSchema(BaseModel):
    name: str

class TagPublicSchema(BaseModel):
    id: int
    name: str