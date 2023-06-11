import streamlit as st

class HomePage():
    def render(self) -> None:
        # タイトルの表示
        st.title("ホーム")

        # Homeは説明中心
        st.write(
            """
            本ツールは、データ可視化に関する基本的な機能を提供するアプリケーションです。
            主に下記機能を提供しています。
            """
        )

        no_col, implement_state_col, func_name_col, func_detail_col, func_page_col = st.columns([1, 1, 1, 3, 2])
        no_col.write("No.")
        implement_state_col.write("実装ステータス")
        func_name_col.write("機能名")
        func_detail_col.write("機能詳細")

        no_col, implement_state_col, func_name_col, func_detail_col, func_page_col = st.columns([1, 1, 1, 3, 2])
        no_col.write("1")
        implement_state_col.write("未実装")
        func_name_col.write("データ準備")
        func_detail_col.write("必要なデータセットを準備します")
        # func_page_col.button("Go")

        no_col.write("2")
        implement_state_col.write("未実装")
        func_name_col.write("データ加工")
        func_detail_col.write("データセットの中で必要な加工処理を行います")
        # func_page_col.button("Go")

        no_col.write("3")
        implement_state_col.write("未実装")
        func_name_col.write("データ可視化")
        func_detail_col.write("準備・加工したデータセットに応じて、可視化を行います")
        # func_page_col.button("Go")


    def _detail_on_clink(self) -> None:
        pass

if __name__ == '__main__':
    HomePage().render()