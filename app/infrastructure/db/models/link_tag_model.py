from sqlalchemy import Column, ForeignKey, Table
from app.infrastructure.db.base import Base

link_tag_table = Table(
    "link_tags",
    Base.metadata,
    Column("link_id", ForeignKey("links.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)