from random import choice
from typing import List

from random_book_names.library import AUTHOR
from random_book_names.library import BOOK_TYPES
from random_book_names.library import FILL_WORDS
from random_book_names.library import OF_SOMETHING
from random_book_names.library import THEME


def chose(collection: List) -> str:
    rnd = choice(collection)
    return rnd


def build_book_title() -> str:
    result = []
    for col in [BOOK_TYPES, FILL_WORDS, THEME, FILL_WORDS, OF_SOMETHING, [',', ';', '|', '-', '.'], AUTHOR]:
        result.append(chose(col))

    return " ".join(result)


def build_library(count: int) -> List[str]:
    result = []
    for i in range(count):
        result.append(build_book_title())
    return result
