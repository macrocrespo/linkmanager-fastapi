from pydantic import BaseModel, HttpUrl

class LinkCreateSchema(BaseModel):
    url: HttpUrl
    title: str
    tags: list[str] = []
    description: str | None = None

class LinkPublicSchema(BaseModel):
    id: int
    url: str
    title: str
    tags: list[str]
    description: str | None = None