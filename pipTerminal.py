#!python3

"""
Pythonista3 Console Terminal.
Version: 2.0.8
Author: DarkRix.
"""

import clipboard, code, console, concurrent.futures, io, lib2to3.main, os, re, requests, shutil, socket, ssl, sys, ui, urllib.error, urllib.request, urllib.parse, platform, time, tarfile, zipfile

ssl._create_default_https_context = ssl._create_unverified_context

class pipTerminal(object):
    def __init__(self):
        self.Command_DIRNAME = ['{}@{}'.format(os.getenv('USER'), platform.node()), '', '']
        self.BackupSTDOUT = sys.stdout
        self.is_Exits = True
        self.HOME_DIC = os.getcwd()
        try:
            os.makedirs(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin'), exist_ok=True)
            os.makedirs(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'bin'), exist_ok=True)
            shutil.copytree(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'bin'), os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin'), dirs_exist_ok=True)
            shutil.rmtree(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'bin'))
            os.makedirs(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'bin'), exist_ok=True)
        except:
            pass

    def _2to3(self, pyArgs):
        try:
            sys.argv[1:] = pyArgs
        except:
            pass
        try:
            lib2to3.main.main('lib2to3.fixes')
        except:
            pass

    def SystemLogo(self):
        console.clear()
        console.set_color(255, 0, 0) # red
        return "{}\n| - pyTerminal v2.0.8 on Python {}\t\t\t|\n| - Author: DarkRix.\t\t\t\t\t\t|\n| - Show All Command: help\t\t\t\t\t|\n{}\n\n".format("-"*41, platform.python_version(), "-"*41)

    def copyFiles(self, FileName, dest):
        try:
            if os.path.isfile(os.path.join(os.getcwd(), FileName)):
                shutil.copy(FileName, dest)
            elif os.path.isdir(os.path.join(os.getcwd(), FileName)):
                shutil.copytree(FileName, dest)
        except:
            pass

    def detect_file(self, file):
        if file.split('.')[-1].lower() == 'py':
            console.set_color(0, 102, 0)
            return file
        elif file.split('.')[-1].lower() == 'cpp':
            console.set_color()
            console.set_color(0, 102, 0)
            return file
        elif file.split('.')[-1].lower() == 'c':
            console.set_color()
            console.set_color(0, 102, 0)
            return file
        elif file.split('.')[-1].lower() == 'java':
            console.set_color()
            console.set_color(0, 102, 0)
            return file
        elif file.split('.')[-1].lower() == 'plist':
            console.set_color()
            console.set_color(0, 10, 255)
            return file
        elif file.split('.')[-1].lower() == 'json':
            console.set_color()
            console.set_color(0, 10, 255)
            return file
        elif file.split('.')[-1].lower() == 'jpg':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'jpeg':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'png':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'bmp':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'gif':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'tiff':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'rgb':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'xbm':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'pbm':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'pgm':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'ppm':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'xbm':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'rast':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'zip':
            console.set_color()
            console.set_color(255, 1, 0)
            return file
        elif file.split('.')[-1].lower() == 'rar':
            console.set_color()
            console.set_color(255, 1, 0)
            return file
        elif file.split('.')[-1].lower() == 'tar':
            console.set_color()
            console.set_color(255, 1, 0)
            return file
        elif file.split('.')[-1].lower() == 'bz2':
            console.set_color()
            console.set_color(255, 1, 0)
            return file
        elif file.split('.')[-1].lower() == 'gz':
            console.set_color()
            console.set_color(255, 1, 0)
            return file
        elif file.split('.')[-1].lower() == 'md':
            console.set_color()
            console.set_color(0, 102, 0)
            return file
        elif file.split('.')[-1].lower() == 'MD':
            console.set_color()
            console.set_color(0, 102, 0)
            return file
        elif file.split('.')[-1].lower() == 'mp4':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'm4v':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'avi':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'webm':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'flv':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'wmv':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'mov':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'm4a':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'mp3':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'ogg':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'aac':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'flac':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'aiff':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'wav':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'wma':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'asf':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'oga':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'alac':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'ape':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'mac':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'tta':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'mka':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'mkv':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'aif':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif file.split('.')[-1].lower() == 'aifc':
            console.set_color()
            console.set_color(255, 0, 0)
            return file
        elif os.path.islink(os.path.join(os.getcwd(), file)):
            console.set_color()
            console.set_color(255, 0, 255)
            return file
        elif os.path.isdir(os.path.join(os.getcwd(), file)):
            console.set_color()
            console.set_color(0, 0, 205)
            return file
        else:
            console.set_color()
            return file

    def delete_Files(self, Name):
        try:
            if os.path.isfile(os.path.join(os.getcwd(), Name)):
                os.remove(Name)
            elif os.path.islink(os.path.join(os.getcwd(), Name)):
                os.unlink(os.path.join(os.getcwd(), Name))
            elif os.path.isdir(os.path.join(os.getcwd(), Name)):
                shutil.rmtree(Name)
        except Exception as e:
            print(e)

    def argument_help(self, Args):
        if Args[1] == '--help':
            Args[1] = '-h'
        if Args[1] == '-h' and Args[0] == 'cat':
            print("Usage: cat [-h] [files [files ...]]")
        if Args[1] == '-h' and Args[0] == 'cd':
            print("Usage: cd [-h] [dir]\n\nChange the Current working directory.")
        if Args[1] == '-h' and Args[0] == 'cp':
            print("Usage: cd [-h] [dir]\n\nChange the Current working directory.")
        if Args[1] == '-h' and Args[0] == 'echo':
            print("Usage: echo [-h]\n\nPrint All arguments to stdout, separated by space")
        if Args[1] == '-h' and Args[0] == 'delclip':
            print('Delete Clipboard')
        if Args[1] == '-h' and Args[0] == 'showip':
            print('Show you are Local & Global iP Adress')
        if Args[1] == '-h' and Args[0] == 'git':
            print('Usage: git clone <url> [path] - clone a remote repository')
        if Args[1] == '-h' and Args[0] == 'la':
            print("Usage: la [-h] [-l] [files [files ...]]")
        if Args[1] == '-h' and Args[0] == 'ls':
            print("Usage: ls [-h] [-l] [files [files ...]]")
        if Args[1] == '-h' and Args[0] == 'ln':
            print("Usage: ln [-h] lhs rhs\n\nCreate Symblic Link.")
        if Args[1] == '-h' and Args[0] == 'mkdir':
            print("Usage: mkdir [-h] [-p] dir [dir ...]\n\nCreate a new directory.\nThe parent directory must specified.")
        if Args[1] == '-h' and Args[0] == 'mv':
            print("Usage: mv [-h] src [src ...] dest\n\nMove(Rename) a file or directory to a new name, or into a new directory.")
        if Args[1] == '-h' and Args[0] == 'ping':
            print("Usage: ping [-h] [-c COUNT] Destination\n\nSend ping to network hosts.")
        if Args[1] == '-h' and Args[0] == 'rm':
            print("Usage: rm [-h] paths [paths ...]")
        if Args[1] == '-h' and Args[0] == 'python':
            print("Usage: python [-h] [file]\n\nPython Interactive Shell.")
        if Args[1] == '-h' and Args[0] == 'py':
            print("Usage: py [-h] [file]\n\nPython Interactive Shell.")
        if Args[1] == '-h' and Args[0] == 'python3':
            print("Usage: python3 [-h] [file]\n\nPython Interactive Shell.")
        if Args[1] == '-h' and Args[0] == 'py3':
            print("Usage: py3 [-h] [file]\n\nPython Interactive Shell.")
        if Args[1] == '-h' and Args[0] == 'wget':
            print("Usage: wget [-h] [url]\n\nA simple File Download.")
        if Args[1] == '-h' and Args[0] == 'unzip':
            print('Usage: unzip [-h] [file]')
        if Args[1] == '-h' and Args[0] == 'zip':
            print('Usage: zip [-h] [OutPutFileName] [Target]')

    def git_clone(self, gitArgs):
        try:
            gitPATH = gitArgs[1]
        except IndexError:
            gitPATH = os.getcwd()
        except:
            gitPATH = os.getcwd()

        if len(gitArgs) > 0:
            rURL = gitArgs[0]
            if rURL.endswith('.git'):
                rURL = rURL[:-4]
            UserName, ProjectName = re.match('https://github.com/(.+)/(.+)', rURL).groups()[0:2]
            gitFileName = gitPATH + '/' + ProjectName
            fURL = 'https://github.com/{USER}/{PROJECT}/archive/master.zip'.format(USER=UserName, PROJECT=ProjectName)
            try:
                RESPONSE_DATA = urllib.request.urlopen(urllib.request.Request(fURL, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; en-la) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 YJApp-ANDROID jp.co.yahoo.android.yjtop/13.91.1','Connection': 'keep-alive','Accept-Encoding': 'identity'})).read()
                master_name = 'master'
            except urllib.error.URLError:
                reURL = 'https://github.com/{}/{}'.format(UserName, ProjectName)
                FFdata = urllib.request.urlopen(urllib.request.Request(reURL, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; en-la) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 YJApp-ANDROID jp.co.yahoo.android.yjtop/13.91.1','Connection': 'keep-alive','Accept-Encoding': 'identity'})).read()
                Pattern = '{}/{}/tree/(.*?)/'.format(UserName, ProjectName)
                master_name = re.findall(Pattern, str(FFdata))[-1]
                ffURL = 'https://codeload.github.com/{}/{}/zip/{}'.format(UserName, ProjectName, master_name)
                RESPONSE_DATA = urllib.request.urlopen(urllib.request.Request(ffURL, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; en-la) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 YJApp-ANDROID jp.co.yahoo.android.yjtop/13.91.1','Connection': 'keep-alive','Accept-Encoding': 'identity', 'HOSTS': 'github.com'})).read()
            with zipfile.ZipFile(io.BytesIO(RESPONSE_DATA), 'r') as Fzip:
                Fzip.extractall(gitPATH+'/.')
            vName = gitFileName + '-' + master_name
            if os.path.exists(vName):
                os.rename(vName, gitFileName)
            print('Done')

    def listdir(self, arg, pwd):
        hOME = os.getenv('HOME')
        if arg == 'long':
            listdirs = sorted(os.listdir())
            len_dir_lists = len(listdirs)
            for lis in range(len_dir_lists):
                if os.path.islink(os.path.join(pwd, listdirs[lis])):
                    try:
                        print('[%s] %s -> %s' % (time.strftime("%Y-%m-%d", time.localtime(os.stat(os.path.join(pwd, listdirs[lis])).st_mtime)),self.detect_file(listdirs[lis]), os.path.realpath(os.path.join(pwd, listdirs[lis])).replace(hOME, '~')))
                    except:
                        continue
                    console.set_color()
                else:
                    try:
                        print('[%s] %s' % (time.strftime("%Y-%m-%d", time.localtime(os.stat(os.path.join(pwd, listdirs[lis])).st_mtime)),self.detect_file(listdirs[lis])))
                    except:
                        continue
                    console.set_color()
        elif arg == None:
            try:
                listdirs = sorted(os.listdir())
                len_dir_list = len(listdirs)
                for li in range(len_dir_list):
                    print(self.detect_file(listdirs[li]))
                    console.set_color()
            except Exception as E:
                print(E)

    def list_stash_bin(self):
        sh_bin_list = sorted(os.listdir(os.path.join(os.getenv('HOME'), 'Documents', 'stash_extensions', 'bin')))
        for DIR_PATH in range(len(sh_bin_list)):
            try:
                if os.path.isdir(sorted(os.path.join(os.getenv('HOME'), 'Documents', 'stash_extensions', 'bin', sh_bin_list[DIR_PATH]))):
                    del sh_bin_list[DIR_PATH]
            except:
                pass
            try:
                if sh_bin_list[DIR_PATH].split('.')[-1].lower() == 'py':
                    sh_bin_list[DIR_PATH] = sh_bin_list[DIR_PATH].replace('.py','')
            except:
                pass
        return ', '.join(sh_bin_list)

    def list_other_cmd(self):
        list = sorted(os.listdir(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin')))
        for d in range(len(list)):
            try:
                if os.path.isdir(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin', list[d])):
                    del list[d]
            except:
                pass
        return ', '.join(list)

    def ping(self, host):
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

    def readfile(self, Name):
        try:
            rfile = open(Name, 'r', encoding='utf-8').read()
            return rfile, '0'
        except:
            try:
                rfile = open(Name, 'rb').read().decode()
                return rfile, '1'
            except:
                try:
                    rfile = open(Name, 'rb').read()
                    return rfile, '1'
                except:
                    pass

    def run_stash_bin(self, cmdName, Sargs):
        try:
            stash_bin_path = os.path.join(os.getenv('HOME'), 'Documents', 'stash_extensions', 'bin')
            Rcommand_name = cmdName + '.py'
            RfileName = os.path.join(stash_bin_path, Rcommand_name)
            RFile_read = open(RfileName, 'r', encoding='utf-8').read()
            sys.argv[1:] = Sargs
            try:
                exec(RFile_read)
            except:
                pass
        except FileNotFoundError:
            pass
        except Exception as E:
            print('ERROR: {}'.format(E))

    def run_other_cmd(self, cmd_name, args):
        try:
            cmd_bin = os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin')
            fileNa = os.path.join(cmd_bin, cmd_name)
            _read = open(fileNa, 'r', encoding='utf-8').read()
            sys.argv[1:] = args
            try:
                exec(_read)
            except:
                pass
        except FileNotFoundError:
            self.run_stash_bin(cmd_name, args)
        except Exception as E:
            print('ERROR: {ERR}'.format(ERR=E))

    def Symbolic_Link(self, Src, Dest):
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

    def wget(self, URL, filename=''):
        user_agent = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.0; en-la; Nexus Build/JPG991) AppleWebKit/511.2 (KHTML, like Gecko) Version/5.0 Mobile/11S444 YJApp-ANDROID jp.co.yahoo.android.yjtop/4.01.1.5'}
        if filename == '':
            output_fileName = urllib.parse.unquote(urllib.parse.unquote(URL.split('/')[-1]))
        else:
            output_fileName = filename
        try:
            ur = urllib.request.urlopen(urllib.request.Request(URL, headers=user_agent))
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
        except:
            try:
                print('downloading.....')
                uu = requests.get(URL, headers=user_agent)
                try:
                    File_size = int(uu.headers['Content-Length'])
                except  (IndexError, ValueError, TypeError):
                    File_size = 0
                if uu.headers['Content-Type'] == 'application/json':
                    with open(output_fileName, 'w') as F:
                        F.write(uu.json())
                    print('save as {}'.format(output_fileName))
                    print("({} bytes)".format(File_size if File_size else "???"))
                else:
                    with open(output_fileName, 'wb') as Fb:
                        Fb.write(uu.content)
                    print('Save as: {}'.format(output_fileName))
                    print("({} bytes)".format(File_size if File_size else "???"))
            except Exception:
                print('Error. URL: {}'.format(URL))

    def help_tar(self):
        print('tar [-h] [-j] [-z] [-x] [file [files ...]]')
        print('Support Archive Type: tar.gz or tar.')
        print('This command is extract only.')

    def TarArgument(self, ARGS):
        try:
            if 'x' in ARGS[1][1:]:
                if 'z' in ARGS[1][1:]:
                    try:
                        tExtract_ALL(os.path.join(os.getcwd(), ARGS[2][0:]), ARGS[1][1:])
                    except:
                        pass
                elif 'j' in ARGS[1][1:]:
                    try:
                        tExtract_ALL(os.path.join(os.getcwd(), ARGS[2][0:]), ARGS[1][1:])
                    except:
                        pass
            elif ARGS[1][1:] == '--help':
                self.help_tar()
            elif 'h' in ARGS[1][1:]:
                self.help_tar()
            else:
                self.help_tar()
        except IndexError:
            self.help_tar()
        except KeyboardInterrupt:
            sys.exit(0)
        except:
            pass

    def ExtractMems(self, mem, ext):
        for tf in mem:
            for pt in ext:
                if tf.name == pt or tf.name.startswith(pt):
                    yield tf

    def tExtract_ALL(self, FName, tArgs, mems=None, Dir='./'):
        if 'z' in tArgs[0]:
            print('Reading gzip file')
            tar = tarfile.open(FName, 'r:gz')
        elif 'j' in tArgs[0]:
            print('Reading bz2 file')
            tar = tarfile.open(FName, 'r:bz2')
        if mems:
            tar.extractall(path=Dir, members=self.ExtractMems(tar, mems))
        else:
            tar.extractall(path=Dir)
        tar.close()
        print('Archive Extracted')

    def ZIPExtractor(self, zFileName):
        if not os.path.isfile(zFileName):
            print('{}: No such File...'.format(zFileName))
        else:
            try:
                pk_Check = open(zFileName, 'rb').read(2)
            except:
                pk_Check = ''
            if pk_Check != b'PK':
                print('{}: Dose not appear to be a ZIPFile.'.format(zFileName))
            if os.path.basename(zFileName).lower().endswith('.zip'):
                ALPath = os.path.splitext(os.path.basename(zFileName))[0]
            else:
                ALPath = os.path.basename(zFileName) + '_UnZIPPED'
            ALPath = os.path.join(os.path.dirname(zFileName), ALPath)
            if (os.path.exists(ALPath)) and not (os.path.isdir(ALPath)):
                print('{}: Destination is not a Directory.'.format(ALPath))
            elif not os.path.exists(ALPath):
                os.makedirs(ALPath, exist_ok=True)
            try:
                ZIPfp = open(zFileName, 'rb')
                ZipF = zipfile.ZipFile(ZIPfp)
                DIR_NAME = [os.path.join(os.path.dirname(_z), '') for _z in ZipF.namelist()]
                COMMON_DIR = os.path.commonprefix(DIR_NAME or ['/'])
                if not COMMON_DIR.endswith('/'):
                    COMMON_DIR = os.path.join(os.path.dirname(COMMON_DIR), '')
                for zNa in ZipF.namelist():
                    zData = ZipF.read(zNa)
                    Fn = zNa
                    if COMMON_DIR:
                        if Fn.startswith(COMMON_DIR):
                            Fn = Fn.split(COMMON_DIR, 1)[-1]
                        elif Fn.startswith('/' + COMMON_DIR):
                            Fn = Fn.split('/' + COMMON_DIR, 1)[-1]
                    Fn = Fn.lstrip('/')
                    Fn = os.path.join(ALPath, Fn)
                    DIRf = os.path.dirname(Fn)
                    if not os.path.exists(DIRf):
                        os.makedirs(DIRf, exist_ok=True)
                    if Fn.endswith('/'):
                        if not os.path.exists(Fn):
                            os.makedirs(Fn, exist_ok=True)
                    else:
                        Fp = open(Fn, 'wb')
                        try:
                            Fp.write(zData)
                        finally:
                            Fp.close()
                    print(Fn)
            except:
                print('{}: ZIP File is Corrupt'.format(zFileName))

    def ZipArchiveCreate(self, ziPFilename, IPath):
        REL_ROOT = os.path.abspath(os.path.dirname(ziPFilename))
        with zipfile.ZipFile(ziPFilename, 'w', zipfile.ZIP_DEFLATED) as OutPutsZip:
            if os.path.isfile(IPath):
                print(IPath)
                ARCHiveName = os.path.relpath(IPath, REL_ROOT)
                OutPutsZip.write(IPath, arcname=ARCHiveName)
            elif os.path.isdir(IPath):
                for Root, Dir, Files in os.walk(IPath):
                    TH_RELROOT = os.path.relpath(Root, REL_ROOT)
                    OutPutsZip.write(Root, arcname=TH_RELROOT)
                    print(TH_RELROOT)
                    for _Fi in Files:
                        Fi_Name = os.path.join(Root, _Fi)
                        if os.path.isfile(Fi_Name):
                            print(Fi_Name)
                            ARCHIVE_NAME = os.path.join(TH_RELROOT, _Fi)
                            OutPutsZip.write(Fi_Name, arcname=ARCHIVE_NAME)

    def delelemnts(self, element):
        while True:
             try:
                 if '' in element:
                      element.remove('')
                 else:
                      break
             except:
                 break
        return element

    def Argument_Paser(self, Args):
        console.set_color()
        try:
            try:
                self.argument_help(Args)
            except IndexError:
                pass
            try:
                if Args[0] == 'help':
                    print('[Default commands]:\nhelp, 2to3, cat, cd, echo, env, git(clone only), la, ls, ln, mkdir, open, ping, rm, tar, uznip, wget, zip, python, python3, pbcopy, pbpaste, delclip, showip, exit\n\n[Third Party commands]:\n' + self.list_other_cmd() + '\n\n[Stash Extensions Commands]:\n' + self.list_stash_bin())
                elif Args[0] == 'cat':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            ViewFile = readfile(Args[1])
                            if ViewFile[1] == '0':
                                print(ViewFile[0])
                            else:
                                print('ERROR: Readed MediaFiles?')
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == '2to3':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            self._2to3(Args[1:])
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'pbcopy':
                    try:
                        clipboard.set('')
                    except:
                        pass
                    concurrent.futures.ThreadPoolExecutor().submit(clipboard.set, str(Args[1]))
                elif Args[0] == 'pbpaste':
                    try:
                        print(clipboard.get())
                    except:
                        pass
                elif Args[0] == 'delclip':
                    try:
                        clipboard.set('')
                    except:
                        pass
                elif Args[0] == 'showip':
                    try:
                        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                            user_agent = {'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.0; en-la; Nexus Build/JPG991) AppleWebKit/511.2 (KHTML, like Gecko) Version/5.0 Mobile/11S444 YJApp-ANDROID jp.co.yahoo.android.yjtop/4.01.1.5'}
                            s.connect(('8.8.8.8', 80))
                            print('Local iP: {}\nGlobal iP: {}'.format(s.getsockname()[0], concurrent.futures.ThreadPoolExecutor().submit(urllib.request.urlopen, urllib.request.Request('http://checkip.amazonaws.com', headers=user_agent)).result().read().decode(errors='ignore').split('\n')[0]))
                    except:
                        pass
                elif Args[0] == 'cd':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            if '$' in Args[1] and '/' in Args[1]:
                                Arg1 = Args[1].replace('$', os.getenv(Args[1].split('$')[1].split('/')[0]))
                                Args[1] = Args.replace(Args[1].split('$')[1].split('/')[0], '')
                            try:
                                if Args[1][0] == '$':
                                    try:
                                        os.chdir(os.getenv(Args[1][1:]))
                                    except Exception as E:
                                        print('ERROR:{}'.format(E))
                                else:
                                    try:
                                        os.chdir(Args[1])
                                    except Exception as E:
                                        print('ERROR:{}'.format(E))
                            except IndexError:
                                try:
                                    os.chdir(self.HOME_DIC)
                                except Exception as E:
                                    print('ERROR:{}'.format(E))
                                if Args[1] == '' or Args[1] == ' ':
                                    try:
                                        os.chdir(self.HOME_DIC)
                                    except Exception as E:
                                        print('ERROR:{}'.format(E))
                            except:
                                pass
                        else:
                            self.argument_help(Args)
                    except:
                        try:
                            os.chdir(self.HOME_DIC)
                        except Exception as E:
                            print('ERROR:{}'.format(E))
                elif Args[0] == 'cp':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            if not '/' in Args[2]:
                                self.copyFiles(os.path.join(os.getcwd(),Args[1]),os.path.join(os.getcwd(), Args[2]))
                            else:
                                self.copyFiles(os.path.join(os.getcwd(),Args[1]), Args[2])
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'echo':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            try:
                                if Args[1][0] == '$':
                                    env_data = os.getenv(Args[1][1:])
                                    if not env_data is None:
                                        print(env_data)
                            except:
                                pass
                        else:
                            self.argument_help(Args)
                    except IndexError:
                        print('')
                    except:
                        pass
                elif Args[0] == 'env':
                    try:
                        for im, vl in os.environ.items():
                            console.set_color(255, 0, 0)
                            print('{}'.format(im), end=': ')
                            console.set_color()
                            print(vl)
                    except:
                        pass
                elif Args[0] == 'git':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            if Args[1] == 'clone':
                                self.git_clone(Args[2:])
                            else:
                                print('git is clone only')
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'la' or Args[0] == 'ls':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            if Args[1] == '-l':
                                self.listdir('long', os.getcwd())
                            else:
                                self.listdir(None, None)
                        else:
                            self.argument_help(Args)
                    except IndexError:
                        self.listdir(None, None)
                    except:
                        pass
                elif Args[0] == 'ln':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            if Args[1] == '-s':
                                try:
                                    if not '/' in Args[2] and not '/' in Args[3]:
                                        self.Symbolic_Link(os.path.join(os.getcwd(), Args[2]), os.path.join(os.getcwd(), Args[3]))
                                    else:
                                        self.Symbolic_Link(Args[2], Args[3])
                                except:
                                    pass
                            else:
                                try:
                                    if not '/' in Args[1]:
                                        self.Symbolic_Link(os.path.join(os.getcwd(), Args[1]), Args[2])
                                    else:
                                        self.Symbolic_Link(Args[1], Args[2])
                                except:
                                    pass
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'pip':
                    try:
                        if not os.path.exists(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin', 'pip')):
                            with open(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin', 'pip'), 'w') as pipF:
                                pipF.write("# -*- coding: utf-8 -*-\nimport re\nimport sys\nfrom pip._internal.cli.main import main\nif __name__ == '__main__':\n    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])\n    sys.exit(main())")
                        cmd_bin_path = os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin')
                        fileNa = os.path.join(cmd_bin_path, 'pip')
                        _read = open(fileNa, 'r', encoding='utf-8').read()
                        sys.argv[1:] = Args[1:]
                        try:
                            exec(_read)
                        except:
                            pass
                        if os.path.exists(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'lib', 'python3.1', 'site-packages')):
                            shutil.copytree(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'lib', 'python3.1', 'site-packages'), os.path.join(os.getenv('HOME'), 'Documents', 'site-packages'), dirs_exist_ok=True)
                            shutil.rmtree(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'lib'))
                            self.__init__()
                    except:
                        pass
                elif Args[0] == 'mkdir':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            if Args[1] == '-p':
                                os.makedirs(Args[2], exist_ok=True)
                            else:
                                os.makedirs(Args[1], exist_ok=True)
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'mv':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            try:
                                shutil.move(Args[1], Args[2])
                            except IndexError:
                                pass
                            except Exception as E:
                                print(E)
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'open':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            try:
                                console.quicklook(Args[1])
                            except Exception as E:
                                print(E)
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'ping':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            try:
                                for _P in range(3):
                                    print(self.ping(Args[1]))
                                    time.sleep(1)
                            except:
                                pass
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'pwd':
                    try:
                        path = os.getcwd()
                    except Exception as E:
                        path = E
                    print(path)
                elif Args[0] == 'rm':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            try:
                                if '$' in Args[1] and '/' in Args[1]:
                                    Arg1 = Args[1].replace('$', os.getenv(Args[1].split('$')[1].split('/')[0]))
                                    Args[1] = Args.replace(Args[1].split('$')[1].split('/')[0], '')
                                if Args[1][0:] == './*':
                                    try:
                                        for _rm in range(len(os.listdir('./'))):
                                            self.delete_Files(os.listdir()[_rm])
                                    except:
                                        pass
                                else:
                                    try:
                                        self.delete_Files(Args[1])
                                    except:
                                        pass
                            except IndexError:
                                try:
                                    self.delete_Files(Args[1])
                                except Exception as E:
                                    print(E)
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'tar':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            self.TarArgument(Args)
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'unzip':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            self.ZIPExtractor(Args[1])
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'python' or Args[0] == 'python3' or Args[0] == 'py' or Args[0] == 'py3':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            if not '/' in Args[1]:
                                file_path = os.path.join(os.getcwd(), Args[1])
                            else:
                                file_path = Args[1]
                            py_file = open(file_path, 'r', encoding='utf-8').read()
                            try:
                                exec(py_file, globals())
                            except:
                                pass
                        else:
                            self.argument_help(Args)
                    except IndexError:
                        try:
                            code.interact()
                        except:
                            pass
                    except:
                        pass
                elif Args[0] == 'wget':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            try:
                                if Args[2] == '-o' or Args[2] == '--output':
                                    self.wget(Args[1], filename=Args[3])
                            except IndexError:
                                self.wget(Args[1])
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'zip':
                    try:
                        if not Args[1] == '-h' or not Args[1] == '--help':
                            try:
                                self.ZipArchiveCreate(Args[1], Args[2])
                            except:
                                pass
                        else:
                            self.argument_help(Args)
                    except:
                        pass
                elif Args[0] == 'exit':
                    print('Exiting.......')
                    self.is_Exits = False
                elif Args[0] == 'clear' or Args[0] == 'cls':
                    console.clear()
                elif Args[0] == '' or Args[0] == ' ':
                    pass
                else:
                    self.run_other_cmd(Args[0], Args[1:])
            except KeyboardInterrupt:
                self.is_Exits = False
        except KeyboardInterrupt:
            self.is_Exits = False

    @ui.in_background
    def main(self):
        self.__init__()
        print(self.SystemLogo())
        console.set_color()
        while self.is_Exits:
            try:
                console.set_color(0, 102, 0)
                self.Command_DIRNAME[2] = ''
                print(self.Command_DIRNAME[0], end='\r', flush=True)
                console.set_color()
                print(':', end='', flush=True)
                console.set_color(0, 10, 255)
                try:
                    self.Command_DIRNAME[2] = os.getcwd().replace(os.getenv('HOME'), '~')
                except Exception as Err:
                   print(Err)
                   try:
                       self.Argument_Paser(['cd', '../'])
                   except:
                      print('Occurred Some Errors,\nExiting.........')
                      sys.exit(0)
                print(self.Command_DIRNAME[2], end='', flush=True)
                console.set_color()
                sys.stdout = self.BackupSTDOUT
                INPUT_Argument = input('$ ')
                if '|' in INPUT_Argument:
                    with io.StringIO() as St:
                        sys.stdout = St
                        self.Argument_Paser(INPUT_Argument.split('|')[0].split(' '))
                        INPUT_Arguments = [INPUT_Argument.replace(' ','').split('|')[1], St.getvalue().replace('\r', '').replace('\n', '')]
                        sys.stdout = self.BackupSTDOUT
                        concurrent.futures.ThreadPoolExecutor().submit(self.Argument_Paser, INPUT_Arguments)
                elif '>>' in INPUT_Argument:
                    with io.StringIO() as St:
                        if '&' in INPUT_Argument:
                            INPUT_Argument = INPUT_Argument.replace(' &', '').replace('&', '')
                            sys.stdout = St
                            INPUT_Arguments = INPUT_Argument.split('>')[0].split(' ')
                            concurrent.futures.ThreadPoolExecutor().submit(self.delelemnts, INPUT_Arguments).result()
                            concurrent.futures.ThreadPoolExecutor().submit(self.Argument_Paser, INPUT_Arguments)
                            ArgV = St.getvalue()
                            sys.stdout = self.BackupSTDOUT
                        else:
                            sys.stdout = St
                            INPUT_Arguments = INPUT_Argument.split('>')[0].split(' ')
                            concurrent.futures.ThreadPoolExecutor().submit(self.delelemnts, INPUT_Arguments).result()
                            self.Argument_Paser(INPUT_Arguments)
                            ArgV = St.getvalue()
                            sys.stdout = self.BackupSTDOUT
                        if '$' in INPUT_Argument.replace(' ', '').split('>>')[1]:
                            FileName = INPUT_Argument.replace(' ', '').split('>>')[1].replace('$', os.getenv(INPUT_Argument.replace(' ', '').split('>>')[1].split('$')[1].split('/')[0])).replace(INPUT_Argument.replace(' ', '').split('>>')[1].split('$')[1].split('/')[0], '')
                        else:
                            FileName = INPUT_Argument.replace(' ', '').split('>>')[1]
                        if "b'" in ArgV:
                            print('ERROR: Readed MediaFiles?')
                        else:
                            with open(FileName, 'wb') as text:
                                text.write(ArgV.encode())
                elif '>' in INPUT_Argument:
                    with io.StringIO() as St:
                        if '&' in INPUT_Argument:
                            INPUT_Argument = INPUT_Argument.replace(' &', '').replace('&', '')
                            sys.stdout = St
                            INPUT_Arguments = INPUT_Argument.split('>')[0].split(' ')
                            concurrent.futures.ThreadPoolExecutor().submit(self.delelemnts, INPUT_Arguments).result()
                            concurrent.futures.ThreadPoolExecutor().submit(self.delelemnts, INPUT_Arguments)
                            ArgV = St.getvalue()
                            sys.stdout = self.BackupSTDOUT
                        else:
                            sys.stdout = St
                            INPUT_Arguments = INPUT_Argument.split('>')[0].split(' ')
                            concurrent.futures.ThreadPoolExecutor().submit(self.delelemnts, INPUT_Arguments).result()
                            self.Argument_Paser(INPUT_Arguments)
                            ArgV = St.getvalue()
                            sys.stdout = self.BackupSTDOUT
                        if '$' in INPUT_Argument.replace(' ', '').split('>')[1]:
                            FileName = INPUT_Argument.replace(' ', '').split('>')[1].replace('$', os.getenv(INPUT_Argument.replace(' ', '').split('>')[1].split('$')[1].split('/')[0])).replace(INPUT_Argument.replace(' ', '').split('>')[1].split('$')[1].split('/')[0], '')
                        else:
                            FileName = INPUT_Argument.replace(' ', '').split('>')[1]
                        if "b'" in ArgV:
                            print('ERROR: Readed MediaFiles?')
                        else:
                            with open(FileName, 'wb') as text:
                                text.write(ArgV.encode())
                elif '&&' in INPUT_Argument:
                    if ' && ' in INPUT_Argument:
                        for argm in INPUT_Argument.split(' && '):
                            concurrent.futures.ThreadPoolExecutor().submit(self.Argument_Paser, [argm])
                    elif '&&' in INPUT_Argument:
                        for argm2 in INPUT_Argument.split('&&'):
                            concurrent.futures.ThreadPoolExecutor().submit(self.Argument_Paser, [argm2])
                elif '&' in INPUT_Argument:
                    INPUT_Argument = INPUT_Argument.replace(' &', '').replace('&', '')
                    concurrent.futures.ThreadPoolExecutor().submit(self.Argument_Paser, INPUT_Argument.split(' '))
                else:
                    self.Argument_Paser(INPUT_Argument.split(' '))
                sys.stdout = self.BackupSTDOUT
            except KeyboardInterrupt:
                sys.stdout = self.BackupSTDOUT
                break
            if not self.is_Exits:
                sys.stdout = self.BackupSTDOUT
                break

if __name__ == '__main__':
    try:
        pipTerminal().main()
    except KeyboardInterrupt:
        pass

