from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String

from config.db import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    original_url = Column(String(512), nullable=False)
    short_url = Column(String(10), unique=True)
    visits = Column(Integer, default=0)
    date_created = Column(DateTime, default=datetime.now)
