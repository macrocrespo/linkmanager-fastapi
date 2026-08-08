from dataclasses import dataclass

@dataclass
class NewTag:
    name: str

@dataclass
class Tag:
    """
    Pure domain entity, already persisted: `id` is required, no `| None`.
    Does not inherit from SQLAlchemy or Pydantic — it doesn't know how it's
    persisted or serialized. That's the Clean Architecture rule: inner
    layers don't depend on infrastructure details.
    """
    id: int
    name: str