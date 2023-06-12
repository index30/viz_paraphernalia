import streamlit as st
import pandas as pd

@st.cache_data
def load_contents():
    # コンテンツ格納
    contents = {}
    # 説明用
    desc_contents = pd.DataFrame({
        "No.": [1,2,3],
        "実装ステータス": ["未実装", "未実装", "未実装"],
        "機能名": ["データ準備", "データ加工", "データ可視化"],
        "機能詳細": ["必要なデータセットの準備を行います", "データセットに必要な加工処理を行います", "準備・加工したデータセットを可視化します"]
    })
    contents["説明用"] = desc_contents
    return contents

class HomePage():
    def __init__(self):
        self.contents = load_contents()

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

        st.dataframe(
            self.contents["説明用"],
            hide_index=True, 
            use_container_width=True
        )

if __name__ == '__main__':
    home = HomePage()
    home.render()