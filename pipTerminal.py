# EASY-INSTALL-ENTRY-SCRIPT: 'pip==20.1.1','console_scripts','pip'
# -*- coding: utf-8 -*-
__requires__ = 'pip==21.0.1'

import sys
from pkg_resources import load_entry_point

while True:
	try:
		sys.argv[1:] = input('Pythonista3: ~# pip ').split(' ')
		load_entry_point('pip==21.0.1', 'console_scripts', 'pip')()
	except KeyboardInterrupt:
		sys.exit()
	except:
		pass
