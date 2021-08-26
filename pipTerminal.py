# -*- coding: utf-8 -*-

import sys, os
from pkg_resources import load_entry_point

pip_version = open(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'pip', '__init__.py'),'r', encoding='utf-8').read().replace('\n\n','\n').split('\n')[1].replace('__version__ = ', '').replace('"','')

while True:
	try:
		sys.argv[1:] = input('Pythonista3: ~# pip ').split(' ')
		load_entry_point('pip=={Version}'.format(Version=pip_version), 'console_scripts', 'pip')()
	except KeyboardInterrupt:
		break
	except:
		pass