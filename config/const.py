from enum import Enum, auto


class SessionKey(Enum):
    PAGE_ID = auto()
    SESSION_ID = auto()

class UtilConst():
    EXT_DICT = {
        "テーブル": ['csv', 'xlsx', 'xls'],
        "画像": ['jpg', 'png']
    }