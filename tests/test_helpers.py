import datetime
import pytest

from .datasets import base36_dataset
from utils.helpers import (
    encode_base36,
    decode_base36,
    generate_url_alias,
    extract_model_id_from_url_alias
)


@pytest.mark.parametrize(
        'int_num',
        [
            1,
            1098922,
            102293748,
            98989998989,
            1000000000000
        ]
    )
def test_encode_int_to_base36(int_num):
    assert encode_base36(int_num) == base36_dataset[int_num]


@pytest.mark.parametrize(
        'base36_value',
        [
            encode_base36(1),
            encode_base36(1098922),
            encode_base36(102293748),
            encode_base36(98989998989),
            encode_base36(1000000000000)
        ]
    )
def test_decode_base36_to_int(base36_value):
    assert base36_dataset[decode_base36(base36_value)] == base36_value


@pytest.mark.parametrize(
        'model_id',
        [
            1,
            6,
            105,
            2111,
            100000
        ]
    )
def test_url_alias_generator(mocker, model_id):
    fake_now = datetime.datetime(2024, 1, 1, 0, 0, 0)

    mocker_datetime = mocker.patch('utils.helpers.datetime')
    mocker_datetime.now.return_value.timestamp.return_value = fake_now.timestamp()

    fake_num = int('%s%s' % (model_id, str(fake_now.timestamp())[:6]))
    assert generate_url_alias(model_id) == encode_base36(fake_num)


@pytest.mark.parametrize(
        'model_id',
        [
            1,
            6,
            105,
            2111,
            100000
        ]
    )
def test_extract_model_id_from_url_alias(model_id):
    alias = generate_url_alias(model_id)
    assert model_id == extract_model_id_from_url_alias(alias)
