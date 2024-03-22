import pytest
import os
import sys

from sqlalchemy import create_engine, schema, orm, text
from sqlalchemy.orm import scoped_session, sessionmaker, close_all_sessions

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from config.db import Base
from config.settings import app_settings
from models import Link
from .datasets import test_link


TEST_DB_SCHEMA = 'test_schema'

engine = create_engine(
    app_settings.db_url,
    future=True,
    pool_size=5,
    max_overflow=10,
    execution_options={'schema_translate_map': {None: TEST_DB_SCHEMA}}
)

sync_session = scoped_session(sessionmaker(autocommit=False,
                                           autoflush=False,
                                           bind=engine))


@pytest.fixture(scope='session', autouse=True)
def db_session():
    with engine.connect().execution_options(
            **{'schema_translate_map': {None: TEST_DB_SCHEMA}}
    ) as connection:

        with connection.begin():
            if not connection.dialect.has_schema(connection, TEST_DB_SCHEMA):
                connection.execute(schema.CreateSchema(TEST_DB_SCHEMA))

            Base.metadata.create_all(bind=connection)

        yield orm.sessionmaker(connection)

        with connection.begin():
            connection.execute(schema.DropSchema(TEST_DB_SCHEMA, cascade=True))


@pytest.fixture(scope='function', autouse=True)
def update_records(db_session):
    with db_session() as conn:
        for table in reversed(Base.metadata.sorted_tables):
            conn.execute(text(f'truncate {TEST_DB_SCHEMA}.{table.name} restart identity cascade;'))
        conn.commit()

    with db_session.begin() as conn:
        conn.add(Link(**test_link))
        conn.flush()

    conn.commit()
    close_all_sessions()


@pytest.fixture(scope='session', autouse=True)
def tst_schema_session(db_session):
    with db_session() as session:
        try:
            yield session
        finally:
            session.close()


@pytest.fixture()
def app():
    from main import app
    app.config.update({
        'TESTING': True,
    })

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
