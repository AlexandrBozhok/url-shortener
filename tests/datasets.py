import datetime

from utils.helpers import generate_url_alias, encode_base36


FAKE_NOW = datetime.datetime(2024, 1, 1, 0, 0, 0)

test_link = {
    'id': 10,
    'original_url': 'https://google.com',
    'short_url': generate_url_alias(10),
    'visits': 0,
    'date_created': FAKE_NOW
}

base36_dataset = {
    1098922: encode_base36(1098922),
    102293748: encode_base36(102293748),
    98989998989: encode_base36(98989998989),
    1: encode_base36(1),
    1000000000000: encode_base36(1000000000000)
}
