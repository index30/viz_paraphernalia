from config.const import PageId
from config.session import SessionManager


class BaseTemplate:
    def __init__(self, page_id: PageId, title: str, ssm: SessionManager) -> None:
        self.page_id = page_id.name
        self.title = title
        self.ssm = ssm

    def render(self) -> None:
        pass