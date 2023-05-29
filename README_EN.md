# Pythonista3 pip configration tool
*no StaSh pip installation tool*

## Installation
*This is code copy & paste Pythonista3 console to run.*
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

# Optional
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

## Optional2
*Use My modified StaSh:*
```Python
import requests as r; exec(r.get('https://raw.githubusercontent.com/CrossDarkrix/Pythonista3_pip_Configration_Tool/main/StaSh/getstash.py').content)
```