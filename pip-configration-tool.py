import os

def main():
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
main()
print('Successful!')