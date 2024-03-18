from typing import Any

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from models import Link
from utils.enums import LinkFilterBy
from utils.helpers import generate_url_alias


class LinkCRUD(Link):

    @classmethod
    def create(cls, original_url: str, session: Session) -> Link:
        query = (
            insert(cls)
            .values(original_url=original_url)
            .returning(cls)
        )
        new_link = session.execute(query).scalar()

        session.flush()

        short_url = generate_url_alias(new_link.id)

        new_link.short_url = short_url

        session.commit()

        return new_link

    @classmethod
    def get_one(
            cls,
            by: LinkFilterBy,
            value: Any,
            session: Session
    ) -> Link | None:
        filters_mapping = {
            LinkFilterBy.ID: lambda v: cls.id == v,
            LinkFilterBy.short_url: lambda v: cls.short_url == v,
            LinkFilterBy.original_url: lambda v: cls.original_url == v
        }

        query = select(cls).where(filters_mapping[by](value))

        link_db = session.execute(query)

        return link_db.scalar()

    @classmethod
    def is_exists(cls):
        pass
