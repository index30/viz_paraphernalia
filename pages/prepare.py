import streamlit as st
from config.const import UtilConst


class PreparePage():
    def __init__(self):
        self._data_type = None

    def set_data_type(self, data_type):
        self._data_type = data_type

    def check_data_type(self, data, col):
        if not data:
            col.warning("データが存在しません")
        else:
            print(data)

    def render(self) -> None:
        # タイトルの表示
        st.title("データ準備")

        # データ準備
        # データ種類の選択
        data_type = st.selectbox(
            "準備するデータの種類",
            ["テーブル", "画像"]
        )
        self.set_data_type(data_type)

        prepare_choice = st.radio("データ生成", ["プリセット", "自分で準備"])
        train_data, validation_data, test_data = None, None, None
        train_col, validation_col, test_col = st.columns([2, 2, 2])

        if prepare_choice == "プリセット":
            pass
        else:
            train_data = train_col.file_uploader(
                f"Upload: 学習用 {self._data_type}データ", 
                type=UtilConst.EXT_DICT[self._data_type], 
                accept_multiple_files=True
            )
            validation_data = validation_col.file_uploader(
                f"Upload: 検証用 {self._data_type}データ", 
                type=UtilConst.EXT_DICT[self._data_type], 
                accept_multiple_files=True
            )
            test_data = test_col.file_uploader(
                f"Upload: テスト用 {self._data_type}データ", 
                type=UtilConst.EXT_DICT[self._data_type], 
                accept_multiple_files=True
            )
        
        self.check_data_type(train_data, train_col)
        self.check_data_type(validation_data, validation_col)
        self.check_data_type(test_data, test_col)

        # TODO: session_stateに、読み込ませたデータの情報をもたせる


    def _detail_on_clink(self) -> None:
        pass

PreparePage().render()