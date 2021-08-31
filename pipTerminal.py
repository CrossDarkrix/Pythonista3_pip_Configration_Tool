#!python3
import code, console, os, requests, shutil, socket, sys, time
from pkg_resources import load_entry_point
from console import set_color as setColor
from six.moves.urllib.request import urlopen

HOME_direct = os.getcwd()

def init():
	try:
		os.makedirs(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin'), exist_ok=True)
		opdic = os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'bin')
		files = os.listdir(opdic)
		for f in range(len(files)):
			shutil.move(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'bin', files[f]), os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin'))
	except:
		pass

def logo():
	clear()
	setColor(255, 0, 0)
	return "- pyTerminal v1.3 on Python3.6.3.\n- Author: DarkRix.\n\n- Show All Commands: help\n"

def _help(lif):
	if lif == 'ln':
		return 'Create Symbolic Link:\nln {Source} {Target}.'
	if lif == 'mv':
		return 'Move File or Directory:\nmv file1 File2\nmv File1 Directory1\nmv Directory1 Directory2.'
	if lif == 'ls':
		return 'List Up File and Directory:\nls -l or ls.'
	if lif == 'la':
		return 'List Up File and Directory:\nla -l or ls.'
	if lif == 'echo':
		return 'Print and Create:\nCreate File: echo > FileName\nPrint ENV: echo $env\nPrint: echo PrintWord.'
	if lif == 'mkdir':
		return 'Create Directory:\nmkdir -p dir/dir or mkdir dir.'
	if lif == 'mv':
		return 'Move File or Directory:\nmv file1 File2\nmv File1 Directory1\nmv Directory1 Directory2.'
	if lif == 'pwd':
		return 'View Current Directory Path:\n pwd.'
	if lif == 'cd':
		return 'Change Directory:\n cd {Directory}.'
	if lif == 'rm':
		return 'Delete File or Directory: rm FileName.'
	if lif == 'cat':
		return 'Read File:\n cat {FileName}.'
	if lif == 'touch':
		return 'Create Empty File:\ntouch {FileName}.'
	if lif == 'cp':
		return 'Copy and Overwrite File:\ncp {file1} {file2} or cp {Dir1} {Dir2}.'
	if lif == 'wget':
		return 'Download File: wget {URL}.'
	if lif == 'python':
		return 'Python Interactive Shell:\npython {File}\npython -m {Module}\npython .'
	if lif == 'python3':
		return 'Python3 Interactive Shell:\npython3 {File}\npython3.'
	if lif == 'ping':
		return 'A Very Simple Ping:\nping {HOST}\nping -c {count} {HOST}'

def detect_file(file):
	if file.split('.')[-1].lower() == 'py':
		setColor(0, 102, 0)
		return file
	elif file.split('.')[-1].lower() == 'cpp':
		setColor()
		setColor(0, 102, 0)
		return file
	elif file.split('.')[-1].lower() == 'c':
		setColor()
		setColor(0, 102, 0)
		return file
	elif file.split('.')[-1].lower() == 'java':
		setColor()
		setColor(0, 102, 0)
		return file
	elif file.split('.')[-1].lower() == 'plist':
		setColor()
		setColor(0, 10, 255)
		return file
	elif file.split('.')[-1].lower() == 'json':
		setColor()
		setColor(0, 10, 255)
		return file
	elif file.split('.')[-1].lower() == 'jpg':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'jpeg':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'png':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'bmp':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'gif':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'tiff':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'rgb':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'xbm':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'pbm':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'pgm':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'ppm':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'xbm':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'rast':
		setColor()
		setColor(255, 0, 0)
		return file
	elif file.split('.')[-1].lower() == 'zip':
		setColor()
		setColor(255, 1, 0)
		return file
	elif file.split('.')[-1].lower() == 'rar':
		setColor()
		setColor(255, 1, 0)
		return file
	elif file.split('.')[-1].lower() == 'tar':
		setColor()
		setColor(255, 1, 0)
		return file
	elif file.split('.')[-1].lower() == 'bz2':
		setColor()
		setColor(255, 1, 0)
		return file
	elif file.split('.')[-1].lower() == 'gz':
		setColor()
		setColor(255, 1, 0)
		return file
	elif file.split('.')[-1].lower() == 'md':
			setColor()
			setColor(0, 102, 0)
			return file
	elif file.split('.')[-1].lower() == 'MD':
			setColor()
			setColor(0, 102, 0)
			return file
	elif file.split('.')[-1].lower() == 'mp4':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'm4v':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'avi':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'webm':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'flv':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'wmv':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'mov':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'm4a':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'mp3':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'ogg':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'aac':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'flac':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'aiff':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'wav':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'wma':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'asf':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'oga':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'alac':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'ape':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'mac':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'tta':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'mka':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'mkv':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'aif':
			setColor()
			setColor(255, 0, 0)
			return file
	elif file.split('.')[-1].lower() == 'aifc':
			setColor()
			setColor(255, 0, 0)
			return file
	elif os.path.islink(os.path.join(os.getcwd(), file)):
		setColor()
		setColor(255, 0, 255)
		return file
	else:
		setColor()
		return file
	
def listdir(arg, pwd):
	hOME = os.getenv('HOME')
	if arg == 'long':
		listdirs = sorted(os.listdir())
		len_dir_lists = len(listdirs)
		for lis in range(len_dir_lists):
			if os.path.islink(os.path.join(pwd, listdirs[lis])):
				print('[%s] %s -> %s' % (time.strftime("%Y-%m-%d", time.localtime(os.stat(os.path.join(pwd, listdirs[lis])).st_mtime)),detect_file(listdirs[lis]), os.path.realpath(os.path.join(pwd, listdirs[lis])).replace(hOME, '~')))
				setColor()
			else:
				print('[%s] %s' % (time.strftime("%Y-%m-%d", time.localtime(os.stat(os.path.join(pwd, listdirs[lis])).st_mtime)),detect_file(listdirs[lis])))
				setColor()
	elif arg == None:
		try:
			listdirs = sorted(os.listdir())
			len_dir_list = len(listdirs)
			for li in range(len_dir_list):
				print(detect_file(listdirs[li]))
				setColor()
		except Exception as E:
			print(E)

def ping(host):
	_p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	_p.settimeout(1)
	f_time = time.time()
	try:
		_p.connect((host, 80))
	except socket.timeout:
		pass
	except Exception as ERR:
		if '22' in str(ERR) or 'argument' in str(ERR):
			pass
		if 'refused' not in str(ERR):
			raise(ERR)
	e_time = time.time()
	_p.close()
	ping_result = 'PING to {HOST} Time: {TIME}ms'.format(HOST=host, TIME=round(((e_time - f_time) * 1000), 2))
	return ping_result

def list_other_cmd():
	list = sorted(os.listdir(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin')))
	for d in range(len(list)):
		try:
			if os.path.isdir(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin', list[d])):
				del list[d]
		except:
			pass
	return ', '.join(list)

def run_other_cmd(cmd_name, args):
	try:
		cmd_bin = os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin')
		fileNa = os.path.join(cmd_bin, cmd_name)
		_read = open(fileNa, 'r', encoding='utf-8').read()
		sys.argv[1:] = args
		try:
			exec(_read)
		except SystemExit:
			pass
	except FileNotFoundError:
		pass
	except Exception as E:
		print('ERROR: {ERR}'.format(ERR=E))

def Symbolic_Link(Src, Dest):
	try:
		if os.path.isfile(Dest):
			print('{DEs} Already Exists'.format(DEs=Dest))
			pass
		if os.path.islink(Dest):
			print('{DEst} Already Linked'.format(DEs=Dest))
			pass
	except:
		pass
	try:
		os.symlink(Src, Dest)
	except Exception as E:
		print('Error: {ERR}.'.format(ERR=E))

def chdirs(Location):
	try:
		os.chdir(Location)
	except Exception as E:
		print('ERROR:{}'.format(E))

def clear():
	console.clear()

def create_empty_file(filename):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('')

def create_file(Fname, Data):
	with open(Fname, 'w', encoding='utf-8') as f:
		f.write(Data)

def delete_Files(Name):
	try:
		if os.path.isfile(os.path.join(os.getcwd(), Name)):
			os.remove(Name)
		elif os.path.islink(os.path.join(os.getcwd(), Name)):
			os.unlink(os.path.join(os.getcwd(), Name))
		elif os.path.isdir(os.path.join(os.getcwd(), Name)):
			shutil.rmtree(Name)
	except Exception as e:
		print(e)
def readfile(Name):
	return open(Name, 'r', encoding='utf-8').read()

def copyFiles(FileName, dest):
	try:
		if os.path.isfile(os.path.join(os.getcwd(), FileName)):
			shutil.copy(FileName, dest)
		elif os.path.isdir(os.path.join(os.getcwd(), FileName)):
			shutil.copytree(FileName, dest)
	except Exception as e:
		pass
def wget(URL):
	try:
		output_fileName = URL.split('/')[-1]
		ur = urlopen(URL)
		md = ur.info()
		try:
			fs = int(md["Content-Length"])
		except (IndexError, ValueError, TypeError):
			fs = 0
		print("Save as: {File} ".format(File=output_fileName))
		print("({Size} bytes)".format(Size=fs if fs else "???"))
		with open(output_fileName, 'wb') as f:
			fs_dl = 0.0
			blsz = 8192
			while True:
				_b = ur.read(blsz)
				if not _b:
					break
				fs_dl += len(_b)
				f.write(_b)
	except Exception:
		print('Unknow Error, URL: {}'.format(URL))

def main():
	print(logo())
	setColor()
	init()
	try:
		while True:
			input_args = input('Pythonista3:~# ').split(' ')
			if input_args[0] == 'ls':
				try:
					if input_args[1] == '-h':
						print(_help('ls'))
						continue
				except:
					pass
				try:
					if input_args[1] == '-l':
						listdir('long', os.getcwd())
						continue
					else:
						listdir(None, None)
						continue
				except:
					listdir(None, None)
					continue
			elif input_args[0] == 'la':
				try:
					if input_args[1] == '-h':
						print(_help('la'))
						continue
				except:
					pass
				try:
					if input_args[1] == '-l':
						listdir('long', os.getcwd())
						continue
					else:
						listdir(None, None)
						continue
				except:
					listdir(None, None)
					continue
			elif input_args[0] == 'ln':
				try:
					if input_args[1] == '-h':
						print(_help('ln'))
						continue
				except:
					continue
				try:
					if not '/' in input_args[1] and not '/' in input_args[2]:
						Symbolic_Link(os.path.join(os.getcwd(), input_args[1]), os.path.join(os.getcwd(), input_args[2]))
						continue
					elif not '/' in input_args[1]:
						Symbolic_Link(os.path.join(os.getcwd(), input_args[1]), input_args[2])
						continue
					else:
						Symbolic_Link(input_args[1], input_args[2])
						continue
				except:
					continue
			elif input_args[0] == 'cd':
				try:
					if input_args[1] == '-h':
						print(_help('cd'))
						continue
				except:
					continue
				try:
					if input_args[1][1:] == '$':
						envpath = os.getenv(input_args[1].replace('$', ''))
						chdirs(envpath)
						continue
					else:
						continue
				except:
					continue
				try:
					if input_args[1] == '':
						chdirs(HOME_direct)
						continue
					else:
						chdirs(input_args[1])
						continue
				except IndexError:
					chdirs(HOME_direct)
					continue
			elif input_args[0] == 'pwd':
				try:
					if input_args[1] == '-h':
						print(_help('pwd'))
						continue
				except:
					continue
				try:
					pwd = os.getcwd()
				except Exception as pwdErr:
					pwd = pwdErr
				print(pwd)
				continue
			elif input_args[0] == 'echo':
				try:
					if input_args[1] == '-h':
						print(_help('echo'))
						continue
				except:
					continue
				try:
					if input_args[1] == '>':
						create_empty_file(input_args[2])
						continue
					if input_args[1][:1] == '$':
						env_data = os.getenv(input_args[1].replace('$', ''))
						if not env_data is None:
							print(env_data)
							continue
						else:
							pass
					if not input_args[1] == '' and input_args[2] == '>':
						create_file(input_args[3], input_args[1])
						continue
					elif not input_args[1] == '':
						print(input_args[1])
						continue
				except:
					if not input_args[1] =='':
						print(input_args[1])
						continue
					else:
						continue
			elif input_args[0] == 'mkdir':
				try:
					if input_args[1] == '-h':
						print(_help('mkdir'))
						continue
				except:
						continue
				if input_args[1] == '-p':
					os.makedirs(input_args[2], exist_ok=True)
					continue
				else:
					os.makedirs(input_args[1], exist_ok=True)
					continue
			elif input_args[0] == 'mv':
				try:
					if input_args[1] == '-h':
						print(_help('mv'))
						continue
				except:
					continue
				try:
					shutil.move(input_args[1], input_args[2])
					continue
				except IndexError:
					continue
				except Exception as Err:
					print(Err)
					continue
			elif input_args[0] == 'rm':
				try:
					if input_args[1] == '-h':
						print(_help('rm'))
						continue
				except:
					continue
				if input_args[1][:1] == '-':
					if input_args[2][:1] == '.':
						try:
							for l in range(len(os.listdir())):
								delete_Files(os.listdir()[l])
							continue
						except:
							try:
								for l in range(len(os.listdir())):
									delete_Files(os.listdir()[l])
								continue
							except:
								continue
				elif input_args[1][:1] == '.':
					try:
						for l in range(len(os.listdir())):
							delete_Files(os.listdir()[l])
							continue
					except:
						try:
							for l in range(len(os.listdir())):
								delete_Files(os.listdir()[l])
							continue
						except:
							continue
				else:
						delete_Files(input_args[1])
						continue
			elif input_args[0] == 'cat':
				try:
					if input_args[1] == '-h':
						print(_help('cat'))
						continue
				except:
					continue
				print(readfile(input_args[1]))
				continue
			elif input_args[0] == 'touch':
				try:
					if input_args[1] == '-h':
						print(_help('touch'))
						continue
				except:
					continue
				create_empty_file(input_args[1])
				continue
			elif input_args[0] == 'cp':
				try:
					if input_args[1] == '-h':
						print(_help('cp'))
						continue
				except:
					continue
				if not '/' in input_args[2]:
					copyFiles(os.path.join(os.getcwd(),input_args[1]),os.path.join(os.getcwd(), input_args[2]))
					continue
				else:
					copyFiles(os.path.join(os.getcwd(),input_args[1]), input_args[2])
					continue
			elif input_args[0] == 'help':
				print('[Default commands]:\nhelp, cat, cd, echo, la, ls, ln, mkdir, ping, rm, wget, python, python3, exit\n\n[Third Party commands]:\n' + list_other_cmd())
			elif input_args[0] == 'clear':
				clear()
				continue
			elif input_args[0] == 'cls':
				clear()
				continue
			elif input_args[0] == 'exit':
				print('Exiting......')
				break
				sys.exit(0)
			elif input_args[0] == 'wget':
				try:
					if input_args[1] == '-h':
						print(_help('wget'))
						continue
				except:
					continue
				wget(input_args[1])
			elif input_args[0] == 'python':
				try:
					if not '/' in input_args[1]:
						file_path = os.path.join(os.getcwd(), input_args[1])
					else:
						file_path = input_args[1]
					py_file = open(file_path, 'r', encoding='utf-8').read()
					ngL = dict(__name__ = '__main__', __file__ = file_path)
					try:
						exec(py_file, ngL)
					except SystemExit:
						pass
					continue
				except:
					try:
						code.interact()
					except SystemExit:
						pass
					continue
			elif input_args[0] == 'python3':
				try:
					if not '/' in input_args[1]:
						file_path = os.path.join(os.getcwd(), input_args[1])
					else:
						file_path = input_args[1]
					py_file = open(file_path, 'r', encoding='utf-8').read()
					ngL = dict(__name__ = '__main__', __file__ = file_path)
					try:
						exec(py_file, ngL)
					except SystemExit:
						pass
					continue
				except:
					try:
						code.interact()
					except SystemExit:
						pass
					continue
			elif input_args[0] == 'ping':
				if input_args[1] == '-h':
					print(_help('ping'))
					continue
				elif input_args[1] == '-c':
					try:
						for G in range(int(input_args[2])):
							print(ping(input_args[3]))
							time.sleep(1)
						continue
					except IndexError:
						pass
				elif input_args[1] == '':
					continue
				else:
					for P in range(3):
						print(ping(input_args[1]))
						time.sleep(1)
					continue
			elif input_args[0] == '':
				continue
			elif input_args[0] == ' ':
				continue
			else:
				run_other_cmd(input_args[0], input_args[1:])
				continue
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == '__main__':
	main()