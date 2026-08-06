from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base class for all ORM models — every table maps to a subclass of this."""