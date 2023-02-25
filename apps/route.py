import streamlit as st

from config.const import SessionKey
from templates.base_template import BaseTemplate
from config.session import SessionManager


class Route:
    def __init__(self, ssm: SessionManager, pages: list[BaseTemplate], nav_label: str = "ページ一覧") -> None:
        self.pages = {page.page_id: page for page in pages}
        self.ssm = ssm
        self.nav_label = nav_label

    def render(self) -> None:
        # ページ選択ボックスを追加
        page_id = st.sidebar.selectbox(
            self.nav_label,
            list(self.pages.keys()),
            format_func=lambda page_id: self.pages[page_id].title,
            key=SessionKey.PAGE_ID.name,
        )

        # ページ描画
        try:
            self.pages[page_id].render()
        except Exception as e:
            st.error(e)