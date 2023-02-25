import streamlit as st
from config.const import PageId
from templates.base_template import BaseTemplate


class HomePage(BaseTemplate):
    def render(self) -> None:
        # タイトルの表示
        st.title(self.title)


    def _detail_on_clink(self) -> None:
        pass