#!python3
import console, os, requests, shutil, sys, time
from pkg_resources import load_entry_point
from console import set_color as setColor

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

def list_other_cmd():
	list = os.listdir(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin'))
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
		exec(_read)
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
	os.chdir(Location)

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

def main():
	init()
	try:
		while True:
			input_args = input('PyTerminal~# ').split(' ')
			if input_args[0] == 'ls':
				if input_args[1] == '-h':
					print('ls -l or ls.')
					continue
				try:
					if input_args[1] == '-l':
						listdir('long', os.getcwd())
					else:
						listdir(None, None)
				except:
					listdir(None, None)
			elif input_args[0] == 'la':
				if input_args[1] == '-h':
					print('la -l or la.')
					continue
				try:
					if input_args[1] == '-l':
						listdir('long', os.getcwd())
					else:
						listdir(None, None)
				except:
					listdir(None, None)
			elif input_args[0] == 'ln':
				if input_args[1] == '-h':
					print('ln -s {source} {desert}')
					continue
				try:
					if input_args[1] == '-s':
						if not '/' in input_args[2] and not '/' in input_args[3]:
							Symbolic_Link(os.path.join(os.getcwd(), input_args[2]), os.path.join(os.getcwd(), input_args[3]))
						elif not '/' in input_args[2]:
							Symbolic_Link(os.path.join(os.getcwd(), input_args[2]), input_args[3])
					elif input_args[1][:1] == '-':
						if not '/' in input_args[2] and not '/' in input_args[3]:
							Symbolic_Link(os.path.join(os.getcwd(), input_args[2]), os.path.join(os.getcwd(), input_args[3]))
						elif not '/' in input_args[2]:
							Symbolic_Link(os.path.join(os.getcwd(), input_args[2]), input_args[3])
					if not '/' in input_args[1] and not '/' in input_args[2]:
						Symbolic_Link(os.path.join(os.getcwd(), input_args[1]), os.path.join(os.getcwd(), input_args[2]))
					elif not '/' in input_args[1]:
						Symbolic_Link(os.path.join(os.getcwd(), input_args[1]), input_args[2])
					else:
						Symbolic_Link(input_args[1], input_args[2])
				except:
					pass
			elif input_args[0] == 'cd':
				try:
					if input_args[1] == '':
						chdirs(HOME_direct)
					else:
						chdirs(input_args[1])
				except IndexError:
					chdirs(HOME_direct)
			elif input_args[0] == 'pwd':
				try:
					pwd = os.getcwd()
				except Exception as pwdErr:
					pwd = pwdErr
				print(pwd)
			elif input_args[0] == 'echo':
				if input_args[1] == '-h':
					print('Create File: echo > FileName\nPrint ENV: echo $env\nPrint: echo PrintWord')
					continue
				try:
					if input_args[1] == '>':
						create_empty_file(input_args[2])
					if input_args[1][:1] == '$':
						env_data = os.getenv(input_args[1].replace('$', ''))
						if not env_data is None:
							print(env_data)
						else:
							pass
					if not input_args[1] == '' and input_args[2] == '>':
						create_file(input_args[3], input_args[1])
					elif not input_args[1] == '':
						print(input_args[1])
				except:
					if not input_args[1] =='':
						print(input_args[1])
					else:
						pass
			elif input_args[0] == 'mkdir':
				if input_args[1] == '-h':
					print('Move File or Directory:\nmv file1 File2\nmv File1 Directory1\nmv Directory1 Directory2')
					continue
				if input_args[1] == '-p':
					os.makedirs(input_args[2], exist_ok=True)
				else:
					os.makedirs(input_args[1], exist_ok=True)
				if input_args[1] == '-h':
					print('mkdir -p dir/dir or mkdir dir')
			elif input_args[0] == 'mv':
				try:
					shutil.move(input_args[1], input_args[2])
				except IndexError:
					pass
				except Exception as Err:
					print(Err)
			elif input_args[0] == 'rm':
				if input_args[1] == '-h':
					print('Delete File or Directory: rm FileName.')
					continue
				if input_args[1][:1] == '-':
					if input_args[2][:1] == '.':
						try:
							for l in range(len(os.listdir())):
								delete_Files(os.listdir()[l])
						except:
							try:
								for l in range(len(os.listdir())):
									delete_Files(os.listdir()[l])
							except:
								pass
				elif input_args[1][:1] == '.':
					try:
						for l in range(len(os.listdir())):
							delete_Files(os.listdir()[l])
					except:
						try:
							for l in range(len(os.listdir())):
								delete_Files(os.listdir()[l])
						except:
							pass
				else:
						delete_Files(input_args[1])
			elif input_args[0] == 'cat':
				if input_args[1] == '-h':
					print('cat File')
					continue
				print(readfile(input_args[1]))
			elif input_args[0] == 'touch':
				if input_args[1] == '-h':
					print('touch FileName.')
					continue
				create_empty_file(input_args[1])
			elif input_args[0] == 'cp':
				if input_args[1] == '-h':
					print('copy file: cp file1 file2 or cp Dir1 Dir2')
					continue
				if not '/' in input_args[2]:
					copyFiles(os.path.join(os.getcwd(),input_args[1]),os.path.join(os.getcwd(), input_args[2]))
				else:
					copyFiles(os.path.join(os.getcwd(),input_args[1]), input_args[2])
			elif input_args[0] == 'help':
				print('help, cat, cd, echo, la, ls, ln, mkdir, rm, exit, ' + list_other_cmd())
			elif input_args[0] == 'clear':
				clear()
			elif input_args[0] == 'cls':
				clear()
			elif input_args[0] == 'exit':
				sys.exit(0)
			else:
				run_other_cmd(input_args[0], input_args[1:])
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == '__main__':
	main()