from dataclasses import dataclass
from app.domain.entities.tag import NewTag, Tag

@dataclass
class NewLink:
    url: str
    title: str
    owner_id: int
    tags: list[NewTag]
    description: str | None = None

@dataclass
class Link:
    id: int
    url: str
    title: str
    owner_id: int
    tags: list[Tag]
    description: str | None = None