from os import chdir as cd
from os import getenv as env
from os import makedirs as mk

HOMEdic = env('HOME')

pip_config = """[global]
prefix = {HOME}/Documents/site-packages/_bin

[user]
prefix = {HOME}/Documents/site-packages/_bin

[site]
prefix = {HOME}/Documents/site-packages/_bin
""".format(HOME=HOMEdic)


cd(HOMEdic)
mk('.config/pip', exist_ok=True)
mk('{HOME}/Documents/site-packages/_bin'.format(HOME=HOMEdic), exist_ok=True)
cd('.config/pip')
with open('pip.conf', mode='w') as f:
	f.write(pip_config)
print('Successful!')