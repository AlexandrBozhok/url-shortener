from crud.link import LinkCRUD
from utils.enums import LinkFilterBy
from .datasets import test_link
from models import Link


class TestLinkCRUD:
    link = Link(**test_link)

    def test_create_link(self, tst_schema_session):
        link_db = LinkCRUD.create(
            self.link.original_url,
            tst_schema_session
        )
        assert link_db is not None
        assert link_db.original_url == self.link.original_url

    def test_get_link(self, tst_schema_session, update_records):
        link_db = LinkCRUD.get_one(
            by=LinkFilterBy.original_url,
            value=self.link.original_url,
            session=tst_schema_session
        )

        assert link_db is not None
        assert link_db.id == self.link.id
        assert link_db.original_url == self.link.original_url
        assert link_db.short_url == self.link.short_url
        assert link_db.visits == self.link.visits
        assert link_db.date_created == self.link.date_created
