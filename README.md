# Pythonista3 pip configration tool
*Pythonista3でStashとは別でpipを使いたい人のためのツール群*

## Installation
*`pip-configration-tool.py`を実行後、*

```Python
import requests as r; exec(r.get('https://bootstrap.pypa.io/get-pip.py').content) 
```

*上記をコンソールにコピペ&実行。*

*実行後Pythonistaを再起動して下さい。*

*再起動後`pipTerminal.py`を実行してエラーがなければ完成。*

*エラーが出た場合: pip==○○○の部分の番号をインストールしたpipのバージョンにしてから実行してください。*

## トラブルシューティング
*・pipのバージョンがわからない: Python Modules -> site-packages -> pipと開き`__init__.py`内の__version__ = ""内に書いてあります。*

*・インストールしたモジュールのコマンドの配置場所がわからない: Python Modules -> site-packages -> binの中に入っています。*

*モジュールのインストール時に警告が出る: -Uオプションをつけてみて下さい。(※Uは大文字です。)*

*モジュールをインストールしたのにpip listに反映されない: モジュールのインストール後は必ずPythonistaを再起動してください。*

*tar.gz形式のモジュールがインストールできない: tar.gzの展開場所が環境変数「TMPDIR」に設定されているためです。現状変更できないのでwheel(.whl)パッケージをインストールして下さい。*

## pip-configration-tool.pyの動作について
*問: 何をしているの?*

*答: モジュールのインストール場所をPython Modules内のsite-packagesに指定する設定ファイルを環境変数「HOME」内の「.config/pip」へ配置しています。*
