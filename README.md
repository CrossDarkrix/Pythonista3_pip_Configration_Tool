# Pythonista3 pip configration tool
*Pythonista3でstashのpipじゃない本物のpipを使いたい人向け*

## Installation
```Python
import requests as r; exec(r.get('https://raw.githubusercontent.com/CrossDarkrix/Pythonista3_pip_Configration_Tool/main/pip-configration-tool.py').content)
```

*`上記でpip-configration-tool.py`を実行後、*

```Python
import requests as r; exec(r.get('https://bootstrap.pypa.io/pip/3.6/get-pip.py').content) 
```

*上記をコンソールにコピペ&実行。*

*実行後Pythonistaを再起動して下さい。*

*再起動後`pipTerminal.py`を実行してエラーがなければ完成。*

![Preview](https://raw.githubusercontent.com/CrossDarkrix/Pythonista3_pip_Configration_Tool/main/images/pip-Terminal_Preview.png)

*おまけ: パッケージを自動選択してアップデートしてくれる`pythonista3_PackagesUpdater`を導入するとアップデートが楽になります。*

*以下を任意の名前でPython Modules -> site-packages -> _binに作成*

```Python
import sys
from pythonista3_PackagesUpdater import main
main(sys.argv[1:])
```

*任意の名前にしたコマンド(例:`pip-updater`) `-h`でヘルプを見れます。*


## トラブルシューティング

*インストールしたモジュールのコマンドの配置場所がわからない: Python Modules -> site-packages -> _binの中に入っています。*

*モジュールのインストール時に警告が出る: -Uオプションをつけてみて下さい。(※Uは大文字です。)*

*モジュールをインストールしたのにpip listに反映されない: モジュールのインストール後は必ずPythonistaを再起動してください。*

*tar.gz形式のモジュールがインストールできない: tar.gzの展開場所が環境変数「TMPDIR」に設定されているためです。現状変更できないのでwheel(.whl)パッケージをインストールして下さい。*

## pip-configration-tool.pyの動作について
*問: 何をしているの?*

*答: モジュールのインストール場所をPython Modules内のsite-packagesに指定する設定ファイルを環境変数「HOME」内の「.config/pip」へ配置しています。*
