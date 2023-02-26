# viz_paraphernalia
様々なデータの可視化ツール

## 構成（予定）
- データ準備
- データ加工
- テーブルデータ
- 画像認識
- 自然言語(余裕があれば)
- 音声認識(余裕があれば)

## 実行
```
$ poetry run streamlit run main.py
```

## 環境準備
Mac環境での準備を想定

- [Poetry](https://python-poetry.org/docs/)の公式サイトを参照して、Poetryをinstall
```
$ curl -sSL https://install.python-poetry.org | python3 -
```

- Pyenvをinstall
```
$ brew install pyenv
```

- Poetryの初期化
```
$ poetry init
$ poetry env use 3.10.10// poetryに使用するPythonバージョンの指定
$ poetry shell // 仮想環境構築
```


