import string
import random


def random_text(length=32, charset=None):
    if not charset:
        charset = string.ascii_letters + string.digits

    return "".join(random.choice(charset) for _ in range(length))


def random_hex(length=32):
    return random_text(length, list(set(string.hexdigits.lower())))
