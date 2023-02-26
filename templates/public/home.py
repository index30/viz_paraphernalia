import streamlit as st
from config.const import PageId
from templates.base_template import BaseTemplate


class HomePage(BaseTemplate):
    def render(self) -> None:
        # タイトルの表示
        st.title(self.title)

        # Homeは説明中心
        st.write(
            """
            本ツールは、データ可視化に関する基本的な機能を提供するアプリケーションです。
            主に下記機能を提供しています。
            - データ準備（未実装）: 必要なデータセットを準備します
            - データ加工（未実装）: データセットの中で必要な加工処理を行います
            - データ可視化（未実装）: 準備・加工したデータセットに応じて、可視化を行います。
            """
        )

        no_col, func_name_col, func_detail_col = st.columns([1, 2, 2])
        


    def _detail_on_clink(self) -> None:
        pass