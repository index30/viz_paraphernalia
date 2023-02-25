from enum import Enum, auto


class SessionKey(Enum):
    PAGE_ID = auto()
    SESSION_ID = auto()


class PageId(Enum):
    HOME = auto()