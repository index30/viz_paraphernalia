import streamlit as st
from config.const import PageId
from templates.base_template import BaseTemplate


class PreparePage(BaseTemplate):
    def render(self) -> None:
        # タイトルの表示
        st.title(self.title)

        # データ準備
        # データ種類の選択
        data_type = st.selectbox(
            "準備するデータの種類",
            ["テーブル", "画像"]
        )


    def _detail_on_clink(self) -> None:
        pass