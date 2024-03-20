import pytest
from sqlalchemy import exc

from crud.link import LinkCRUD
from models import Link
from .datasets import test_link


def test_request_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<div class="form-div">' in response.data


def test_redirect_to_own_url(client, mocker):
    link = Link(**test_link)
    mocker.patch.object(LinkCRUD, 'get_one', return_value=link)
    response = client.get(f'{link.short_url}')

    assert response.status_code == 302
    assert response.location == link.original_url


def test_add_link_already_exists(client, mocker):
    link = Link(**test_link)
    mocker.patch.object(LinkCRUD, 'get_one', return_value=link)

    response = client.post(
        '/add_link',
        data={'original_url': link.original_url}
    )
    assert response.status_code == 200
    assert bytes(link.original_url.encode()) in response.data


def test_add_link_not_exists(client, mocker):
    link = Link(**test_link)
    mocker.patch.object(LinkCRUD, 'get_one', return_value=None)
    mocker.patch.object(LinkCRUD, 'create', return_value=link)

    response = client.post(
        '/add_link',
        data={'original_url': link.original_url}
    )

    assert response.status_code == 200
    assert bytes(link.original_url.encode()) in response.data


@pytest.mark.xfail(raises=exc.SQLAlchemyError)
def test_add_link_exception(client, mocker):
    link = Link(**test_link)

    mocker.patch(
            'routers.base.LinkCRUD.create',
            side_effect=exc.SQLAlchemyError
    )
    response = client.post(
        '/add_link',
        data={'original_url': link.original_url}
    )

    assert response.status_code == 500
