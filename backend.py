import validators
from hashids import Hashids
from config import SECRET_KEY


def is_valid_url(url):
    return validators.url(url)


def shorten(url_id):
    return Hashids(salt=SECRET_KEY, min_length=8).encode(url_id)


