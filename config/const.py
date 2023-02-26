from enum import Enum, auto


class SessionKey(Enum):
    PAGE_ID = auto()
    SESSION_ID = auto()

class UtilConst(Enum):
    EXT_DICT = {
        "テーブル": ['csv', 'xlsx', 'xls'],
        "画像": ['jpg', 'png']
    }

class PageId(Enum):
    HOME = auto()
    PREPARE = auto()