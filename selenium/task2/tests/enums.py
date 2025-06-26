from enum import StrEnum


class Language(StrEnum):
    RU = "ru"
    EN = "en"


class Game(StrEnum):
    WITCHER = "The Witcher"
    FALLOUT = "Fallout"


class URL(StrEnum):
    STEAM_TEST_URL = "https://store.steampowered.com/"
