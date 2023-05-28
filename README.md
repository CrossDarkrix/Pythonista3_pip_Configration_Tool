# Pythonista3 pip configration tool
*Pythonista3でstashのpipじゃない本物のpipを使いたい人向け*

## Installation
```Python
import requests as r; exec(r.get('https://tinyurl.com/Setup-pipTerminal').content)
```

*上記で`Setup-pipTerminal.py`を実行後、Pythonistaを再起動して下さい。*


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

*モジュールをインストールしたのにpip listに反映されない: モジュールのインストール後は必ずPythonistaを再起動してください。*

*tar.gz形式のモジュールがインストールできない: tar.gzの展開場所が環境変数「TMPDIR」に設定されているためです。現状変更できないのでwheel(.whl)パッケージをインストールして下さい。*

## pip-configration-tool.pyの動作について
*問: 何をしているの?*

*答: モジュールのインストール場所をPython Modules内のsite-packagesに指定する設定ファイルを環境変数「HOME」内の「.config/pip」へ配置しています。*

## おまけ

*StaShの２０２１年度版のPythonista3.4暫定対処版を使う場合*

```Python
import requests as r; exec(r.get('https://raw.githubusercontent.com/CrossDarkrix/Pythonista3_pip_Configration_Tool/main/StaSh/getstash.py').content)
```

## English version

# Pythonista3 pip configration tool
*no StaSh pip installation tool*

## Installation
*running to*
```Python
import requests as r; exec(r.get('https://tinyurl.com/Setup-pipTerminal').content)
```
*And restart Pythonista.*
*Installation Done!*

![Preview](https://raw.githubusercontent.com/CrossDarkrix/Pythonista3_pip_Configration_Tool/main/images/pip-Terminal_Preview.png)

# Troubleshooting
*Do no know installed module command path. -> Modules install command path to: "~/Documents/site-packages/_bin".*
*not showing installed module to "pip list". -> Please restart pythonista*

*tar.gz moddule not installing. -> pythonista is not supported tarball module.* 

# Optinal
*`pythonista3_PackagesUpdater` is Easy all module auto updating tool*
*download pythonista3_PackagesUpdater.py to "~/Documents/site-packages/pythonista3_PackagesUpdater.py"*

*set Any command name. Example: "~/Documents/site-packages/_bin/pupdate"*
*Write "pupdate" conent:*
```Python
import sys
from pythonista3_PackagesUpdater import main
main(sys.argv[1:])
```
*help showing to "pupdate --help or pupdate -h".*


## Optinal2
*Use My modified StaSh:*
```Python
import requests as r; exec(r.get('https://raw.githubusercontent.com/CrossDarkrix/Pythonista3_pip_Configration_Tool/main/StaSh/getstash.py').content)
```