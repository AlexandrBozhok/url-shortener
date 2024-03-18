import string

from datetime import datetime


def encode_base36(value: int) -> str:
    """Converts a positive integer into a base36 string"""
    char_set = string.digits + string.ascii_lowercase

    result = ''
    while not result or value > 0:
        value, i = divmod(value, 36)
        result = char_set[i] + result
    return result


def decode_base36(value: str) -> int:
    """Converts a base36 string into a positive integer"""
    return int(value, 36)


def generate_url_alias(model_id: int) -> str:
    ts = str(datetime.now().timestamp())
    num = f'{model_id}{ts[:6]}'

    return encode_base36(int(num))


def extract_model_id_from_url_alias(url_alias: str) -> int:
    num = decode_base36(url_alias)

    return int(str(num)[:-6])
