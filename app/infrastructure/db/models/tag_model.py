from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.db.base import Base
from app.infrastructure.db.models.link_tag_model import link_tag_table

class TagModel(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    links: Mapped[list["LinkModel"]] = relationship(secondary=link_tag_table, back_populates="tags")