from enum import Enum


class LinkFilterBy(str, Enum):
    ID = 'id'
    original_url = 'original_url'
    short_url = 'short_url'
