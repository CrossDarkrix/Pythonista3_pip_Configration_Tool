import os, urllib.request, pkgutil, shutil, tempfile, argparse, importlib, sys
from base64 import b85decode

def setting_pip():
    FirstDic = os.getcwd()
    HOMEDic = os.getenv('HOME')
    pip_config = """[global]
prefix={HOME}/Documents/site-packages/

[user]
prefix={HOME}/Documents/site-packages/

[site]
prefix={HOME}/Documents/site-packages/""".format(HOME=HOMEDic)

    os.chdir(HOMEDic)
    os.makedirs(os.path.join('.config', 'pip'), exist_ok=True)
    os.makedirs(os.path.join(HOMEDic, 'Documents', 'site-packages', '_bin'), exist_ok=True)
    os.chdir(os.path.join('.config', 'pip'))
    with open('pip.conf', 'w') as f:
        f.write(pip_config)
    os.chdir(FirstDic)

def installation_pipTerminal():
    with open(os.path.join(os.getenv('HOME'), 'Documents', 'pipTerminal.py'), 'w') as terminal:
        terminal.write(urllib.request.urlopen('https://raw.githubusercontent.com/CrossDarkrix/Pythonista3_pip_Configration_Tool/main/pipTerminal.py').read().decode(errors='ignore'))

def installation_realpip():
    with open(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'setuppip.py'), 'w') as fpip:
        fpip.write(urllib.request.urlopen('https://bootstrap.pypa.io/get-pip.py').read().decode(errors='ignore'))
    with open(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'setuppip.py'), 'r') as _rp:
        from setuppip import main
        main()
    os.remove(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'setuppip.py'))

def main():
    print('Settingup pip conf file.........')
    setting_pip()
    print('Successful setting pip configration!')
    print('Save pipTerminal.........')
    installation_pipTerminal()
    print('Successful Save pipTerminal! save path: ~/Documents/pipTerminal.py')
    print('Install Real pip.........')
    installation_realpip()
    print('All Installation Done!')
    print('Please Restart Pythonista!')

main()