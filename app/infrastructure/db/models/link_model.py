from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.infrastructure.db.base import Base
from app.infrastructure.db.models.link_tag_model import link_tag_table

class LinkModel(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(2048))
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    owner: Mapped["UserModel"] = relationship(back_populates="links")
    tags: Mapped[list["TagModel"]] = relationship(secondary=link_tag_table, back_populates="links")
