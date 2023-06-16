#!python3
import collections # for the namedtuple fileinfo
import datetime    # to format timestamps
import editor      # to open files
import errno       # for OSError codes
import os.path     # to navigate the file structure
import Image       # for thumbnail creation
import pwd         # to get names for UIDs
import sound       # to play audio files
import stat        # to analyze stat results
import io
import ui          # duh
import webbrowser
import code, console, clipboard, concurrent.futures, os, re, shutil, socket, sys, urllib.request, time, tarfile, zipfile, urllib.parse, ssl, socket, requests, ui, platform, qrcode
from lib2to3.main import main as _2to3_main
from io import BytesIO, StringIO
from urllib.error import URLError

ssl._create_default_https_context = ssl._create_unverified_context

Command_DIRNAME = ['{}@{}'.format(os.getenv('USER'), platform.node()), '', '']
HOME_DIC = os.getcwd()
is_Exits = True

class QRCodeView(object):
    def __init__(self, url):
        self.url = url
        self.filename = 'tmpQR.png'
        self.tmpFolder = tempfile.gettempdir()
        self.tempPath = os.path.join(self.tmpFolder, self.filename)
        qrcode.make(self.url).save(self.tempPath)

    def __enter__(self):
        return self.tempPath

    def __exit__(self, _, __, ___):
        os.remove(self.tempPath)

class ImageLoad(object):
    def __init__(self):
        self.ImageData = None
        self.Image = Image
        Image.Image.tostring = self.tostring

    def tostring(self):
        return self.ImageData.tobytes()

    def open(self, fp):
        try:
            self.ImageData = self.Image.open(fp).convert('RGBA')
            return self.Image.open(fp).convert('RGBA')
        except:
            self.ImageData = self.Image.open(fp)
            return self.Image.open(fp)

class pipTerminal(object):
    def __init__(self):
        self.Command_DIRNAME = ['{}@{}'.format(os.getenv('USER'), platform.node()), '', '']
        self.BackupSTDOUT = sys.stdout
        self.is_Exits = True
        self.HOME_DIC = os.getcwd()
        self.printed_STDOUT = [None]
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
            print("Usage: ping [-h] [iP]\nDestination\n\nSend ping to network hosts.")
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
        if Args[1] == '-h' and Args[0] == 'qrcode':
            print('Usage: qrcode [-h] [URL]')

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
        if Name.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.rgb', '.pgm', '.pbm', '.ppm', '.xbm')):
            rfile = ImageLoad().open(Name)
            self.printed_STDOUT[0] = rfile
            return '3'
        else:
            rfile = open(Name, 'rb').read()
            self.printed_STDOUT[0] = rfile
            return '0'

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
                    print('[Default commands]:\nhelp, 2to3, cat, cd, echo, env, git(clone only), la, ls, ln, mkdir, open, ping, rm, tar, uznip, wget, zip, python, python3, qrcode,  pbcopy, pbpaste, delclip, showip, exit\n\n[Third Party commands]:\n' + self.list_other_cmd() + '\n\n[Stash Extensions Commands]:\n' + self.list_stash_bin())
                elif Args[0] == 'cat':
                    try:
                        if not Args[1] == '-h':
                            ViewFile = self.readfile(Args[1])
                            if ViewFile[0] == '0':
                                try:
                                    print(self.printed_STDOUT[0].decode())
                                except:
                                    print('Error: Read Text File?')
                            elif ViewFile[0] == '3':
                               print('{}'.format(console.show_image(Args[1])).split('None')[0])
                        else:
                            pass
                    except Exception as E:
                        print(E)
                        pass
                elif Args[0] == '2to3':
                    try:
                        if not Args[1] == '-h':
                            self._2to3(Args[1:])
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'pbcopy':
                    try:
                        clipboard.set_image(Args[1])
                    except:
                        clipboard.set(str(Args[1]))
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
                        if not Args[1] == '-h':
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
                            pass
                    except:
                        try:
                            os.chdir(self.HOME_DIC)
                        except Exception as E:
                            print('ERROR:{}'.format(E))
                elif Args[0] == 'cp':
                    try:
                        if not Args[1] == '-h':
                            if not '/' in Args[2]:
                                self.copyFiles(os.path.join(os.getcwd(),Args[1]),os.path.join(os.getcwd(), Args[2]))
                            else:
                                self.copyFiles(os.path.join(os.getcwd(),Args[1]), Args[2])
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'echo':
                    try:
                        if not Args[1] == '-h':
                            try:
                                if Args[1][0] == '$':
                                    env_data = os.getenv(Args[1][1:])
                                    if not env_data is None:
                                        print(env_data)
                            except:
                                pass
                        else:
                            pass
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
                        if not Args[1] == '-h':
                            if Args[1] == 'clone':
                                self.git_clone(Args[2:])
                            else:
                                print('git is clone only')
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'la' or Args[0] == 'ls':
                    try:
                        if not Args[1] == '-h':
                            if Args[1] == '-l':
                                self.listdir('long', os.getcwd())
                            else:
                                self.listdir(None, None)
                        else:
                            pass
                    except IndexError:
                        self.listdir(None, None)
                    except:
                        pass
                elif Args[0] == 'ln':
                    try:
                        if not Args[1] == '-h':
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
                            pass
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
                        if not Args[1] == '-h':
                            if Args[1] == '-p':
                                os.makedirs(Args[2], exist_ok=True)
                            else:
                                os.makedirs(Args[1], exist_ok=True)
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'qrcode':
                    try:
                        if not Args[1] == '-h':
                            with QRCodeView(Args[1]) as QR:
                                print('{}'.format(console.show_image(QR)).split('None')[0])
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'mv':
                    try:
                        if not Args[1] == '-h':
                            try:
                                shutil.move(Args[1], Args[2])
                            except IndexError:
                                pass
                            except Exception as E:
                                print(E)
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'open':
                    try:
                        if not Args[1] == '-h':
                            try:
                                console.quicklook(Args[1])
                            except Exception as E:
                                print(E)
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'ping':
                    try:
                        if not Args[1] == '-h':
                            try:
                                for _P in range(3):
                                    print(self.ping(Args[1]))
                                    time.sleep(1)
                            except:
                                pass
                        else:
                            pass
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
                        if not Args[1] == '-h':
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
                            pass
                    except:
                        pass
                elif Args[0] == 'tar':
                    try:
                        if not Args[1] == '-h':
                            self.TarArgument(Args)
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'unzip':
                    try:
                        if not Args[1] == '-h':
                            self.ZIPExtractor(Args[1])
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'python' or Args[0] == 'python3' or Args[0] == 'py' or Args[0] == 'py3':
                    try:
                        if not Args[1] == '-h':
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
                            pass
                    except IndexError:
                        try:
                            code.interact()
                        except:
                            pass
                    except:
                        pass
                elif Args[0] == 'wget':
                    try:
                        if not Args[1] == '-h':
                            try:
                                if Args[2] == '-o' or Args[2] == '--output':
                                    self.wget(Args[1], filename=Args[3])
                            except IndexError:
                                self.wget(Args[1])
                        else:
                            pass
                    except:
                        pass
                elif Args[0] == 'zip':
                    try:
                        if not Args[1] == '-h':
                            try:
                                self.ZipArchiveCreate(Args[1], Args[2])
                            except:
                                pass
                        else:
                            pass
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
    def main(self, cmd=''):
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
                if cmd == '':
                    INPUT_Argument = input('$ ')
                elif cmd == 'clear':
                    INPUT_Argument = cmd
                    cmd = ''
                else:
                    INPUT_Argument = cmd
                    cmd = 'clear'
                if '|' in INPUT_Argument:
                    with io.StringIO() as St:
                        sys.stdout = St
                        self.Argument_Paser(INPUT_Argument.split('|')[0].split(' '))
                        if not self.printed_STDOUT[0] == None:
                            printed = self.printed_STDOUT[0]
                            try:
                                INPUT_Arguments = [INPUT_Argument.replace(' ','').split('|')[1], printed]
                            except:
                                INPUT_Arguments = [INPUT_Argument.replace(' ','').split('|')[1], printed]
                        else:
                            printed = St.getvalue()
                            INPUT_Arguments = [INPUT_Argument.replace(' ','').split('|')[1], printed]
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
                            if not self.printed_STDOUT[0] == None:
                                ArgV = self.printed_STDOUT[0]
                            else:
                                ArgV = St.getvalue()
                            sys.stdout = self.BackupSTDOUT
                        else:
                            sys.stdout = St
                            INPUT_Arguments = INPUT_Argument.split('>')[0].split(' ')
                            concurrent.futures.ThreadPoolExecutor().submit(self.delelemnts, INPUT_Arguments).result()
                            self.Argument_Paser(INPUT_Arguments)
                            if not self.printed_STDOUT[0] == None:
                                ArgV = self.printed_STDOUT[0]
                            else:
                                ArgV = St.getvalue()
                            sys.stdout = self.BackupSTDOUT
                        if '$' in INPUT_Argument.replace(' ', '').split('>>')[1]:
                            FileName = INPUT_Argument.replace(' ', '').split('>>')[1].replace('$', os.getenv(INPUT_Argument.replace(' ', '').split('>>')[1].split('$')[1].split('/')[0])).replace(INPUT_Argument.replace(' ', '').split('>>')[1].split('$')[1].split('/')[0], '')
                        else:
                            FileName = INPUT_Argument.replace(' ', '').split('>>')[1]
                        if type(ArgV) == type(bytes()):
                            with open(FileName, 'ab') as text:
                                text.write(ArgV)
                        elif type(ArgV) == Image.Image:
                            ArgV.save(FileName, 'png')
                        else:
                            with open(FileName, 'ab') as text:
                                text.write(ArgV.encode())
                elif '>' in INPUT_Argument:
                    with io.StringIO() as St:
                        if '&' in INPUT_Argument:
                            INPUT_Argument = INPUT_Argument.replace(' &', '').replace('&', '')
                            sys.stdout = St
                            INPUT_Arguments = INPUT_Argument.split('>')[0].split(' ')
                            concurrent.futures.ThreadPoolExecutor().submit(self.delelemnts, INPUT_Arguments).result()
                            concurrent.futures.ThreadPoolExecutor().submit(self.delelemnts, INPUT_Arguments)
                            if not self.printed_STDOUT[0] == None:
                                ArgV = self.printed_STDOUT[0]
                            else:
                                ArgV = St.getvalue()
                            sys.stdout = self.BackupSTDOUT
                        else:
                            sys.stdout = St
                            INPUT_Arguments = INPUT_Argument.split('>')[0].split(' ')
                            concurrent.futures.ThreadPoolExecutor().submit(self.delelemnts, INPUT_Arguments).result()
                            self.Argument_Paser(INPUT_Arguments)
                            if not self.printed_STDOUT[0] == None:
                                ArgV = self.printed_STDOUT[0]
                            else:
                                ArgV = St.getvalue()
                            sys.stdout = self.BackupSTDOUT
                        if '$' in INPUT_Argument.replace(' ', '').split('>')[1]:
                            FileName = INPUT_Argument.replace(' ', '').split('>')[1].replace('$', os.getenv(INPUT_Argument.replace(' ', '').split('>')[1].split('$')[1].split('/')[0])).replace(INPUT_Argument.replace(' ', '').split('>')[1].split('$')[1].split('/')[0], '')
                        else:
                            FileName = INPUT_Argument.replace(' ', '').split('>')[1]
                        if type(ArgV) == type(bytes()):
                            with open(FileName, 'wb') as text:
                                text.write(ArgV)
                        elif type(ArgV) == Image.Image:
                            ArgV.save(FileName, 'png')
                        else:
                            print(type(ArgV))
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
                self.printed_STDOUT = [None]
            except KeyboardInterrupt:
                sys.stdout = self.BackupSTDOUT
                self.printed_STDOUT = [None]
                break
            if not self.is_Exits:
                sys.stdout = self.BackupSTDOUT
                self.printed_STDOUT = [None]
                break

def full_path(path):
    # Return absolute path with expanded ~s, input path assumed relative to cwd
    return os.path.realpath(os.path.abspath(os.path.expanduser(path)))

def rel_to_docs(path):
    # Return path relative to script library (~/Documents)
    return os.path.relpath(full_path(path), os.path.expanduser("~/Documents"))

def rel_to_app(path):
    # Return path relative to app bundle (~/Pythonista.app)
    return os.path.relpath(full_path(path), os.path.expanduser("~/Pythonista.app"))

# get location of current script, fall back to ~ if necessary

SCRIPT_ROOT = full_path("~") if sys.argv[0] == "prompt" else os.path.dirname(sys.argv[0])

if not os.path.exists(os.path.join(SCRIPT_ROOT, "temp")):
    os.mkdir(os.path.join(SCRIPT_ROOT, "temp"))

# list of file size units
SIZE_SUFFIXES = "bytes KiB MiB GiB TiB PiB EiB ZiB YiB".split()

# dict of known file extensions
FILE_EXTS = {
    "aac":           "Apple Audio",
    "aif":           "AIFF Audio",
    "aiff":          "AIFF Audio",
    "app":           "Mac or iOS App Bundle",
    "authors":       "Author List",
    "avi":           "AVI Video",
    "bin":           "Binary Data",
    "bmp":           "Microsoft Bitmap Image",
    "build":         "Build Instructions",
    "bundle":        "Bundle",
    "bz2":           "Bzip2 Archive",
    "c":             "C Source Code",
    "cache":         "Data Cache",
    "caf":           "CAF Audio",
    "cfg":           "Configuration File",
    "changelog":     "Changelog",
    "changes":       "Changelog",
    "command":       "Shell Script",
    "conf":          "Configuration File",
    "contribs":      "Contributor List",
    "contributors":  "Contributor List",
    "copyright":     "Copyright Notice",
    "copyrights":    "Copyright Notice",
    "cpgz":          "CPGZ Archive",
    "cpp":           "C++ Source Code",
    "css":           "Cascading Style Sheet",
    "csv":           "Comma-separated Values",
    "dat":           "Data",
    "db":            "Database",
    "dmg":           "Mac Disk Image",
    "doc":           "MS Word Document",
    "docx":          "MS Word Document (XML-based)",
    "dot":           "MS Word Template",
    "dotx":          "MS Word Template (XML-based)",
    "exe":           "Windows Executable",
    "fon":           "Bitmap Font",
    "gif":           "GIF Image",
    "git":           "Git Data",
    "gitignore":     "Git File Ignore List",
    "gz":            "Gzip Archive",
    "gzip":          "Gzip Archive",
    "h":             "C Header Source Code",
    "hgignore":      "Mercurial File Ignore List",
    "hgsubstate":    "Mercurial Substate",
    "hgtags":        "Mercurial Tags",
    "hpp":           "C++ Header Source Code",
    "htm":           "HTML File",
    "html":          "HTML File",
    "icns":          "Apple Icon Image",
    "in":            "Configuration File",
    "ini":           "MS INI File",
    "install":       "Install Instructions",
    "installation":  "Install Instructions",
    "itunesartwork": "iOS App Logo",
    "jpeg":          "JPEG Image",
    "jpg":           "JPEG Image",
    "js":            "JavaScript",
    "json":          "JSON File",
    "license":       "License",
    "m4a":           "MPEG-4 Audio",
    "m4r":           "MPEG-4 Ringtone",
    "m4v":           "MPEG-4 Video",
    "makefile":      "Makefile",
    "md":            "Markdown Text",
    "mov":           "Apple MOV Video",
    "mp3":           "MPEG-3 Audio",
    "mp4":           "MPEG-4 Video",
    "nib":           "Mac or iOS Interface File",
    "odf":           "ODF Document",
    "odp":           "ODF Slideshow",
    "ods":           "ODF Spreadsheet",
    "odt":           "ODF Text",
    "ogg":           "Ogg Vorbis Audio",
    "otf":           "OpenType Font",
    "pages":         "Apple Pages Document",
    "pdf":           "PDF Document",
    "php":           "PHP Script",
    "pkl":           "Python Pickle Data",
    "plist":         "Apple Property List",
    "png":           "PNG Image",
    "pps":           "MS PowerPoint Template",
    "ppsx":          "MS PowerPoint Template (XML-based)",
    "ppt":           "MS PowerPoint Slideshow",
    "pptx":          "MS PowerPoint Slideshow (XML-based)",
    "pxd":           "Pyrex Script",
    "pxi":           "Pyrex Script",
    "py":            "Python Script",
    "pyc":           "Python Bytecode",
    "pyo":           "Python Bytecode",
    "pytheme":       "Pythonista Code Theme",
    "pyui":          "Pythonista UI File",
    "pyx":           "Pyrex Script",
    "rar":           "RAR Archive",
    "readme":        "Read Me File",
    "rst":           "reStructured Text",
    "rtf":           "RTF Document",
    "sh":            "Shell Script",
    "src":           "Source Code",
    "svg":           "Scalable Vector Graphic",
    "tar":           "Tar Archive",
    "tgz":           "Tar Ball",
    "ttc":           "TrueType Font Collection",
    "ttf":           "TrueType Font",
    "txt":           "Plain Text",
    "version":       "Version Details",
    "wav":           "Waveform Audio",
    "xls":           "MS Excel Spreadsheet",
    "xlsx":          "MS Excel Spreadsheet (XML-based)",
    "xlt":           "MS Excel Template",
    "xltx":          "MS Excel Template (XML-based)",
    "xml":           "XML File",
    "yml":           "YML File",
    "z":             "Compressed Archive",
    "zip":           "Zip Archive"
             }

# dict of known file type groups and extensions
FILE_TYPES = {
    "app":       "app exe nib pytheme pyui",
    "archive":   "bundle bz2 cpgz dmg gz gzip rar tar tgz z zip",
    "audio":     "aac aif aiff caf m4a m4r mp3 ogg wav",
    "code":      """c command cpp css h hpp js json makefile pxd pxi py pyx
                    sh src""",
    "code_tags": "htm html php plist xml",
    "data":      "bin cache dat db pkl pyc pyo",
    "font":      "fon otf ttc ttf",
    "git":       "git gitignore",
    "image":     "bmp gif icns itunesartwork jpg jpeg png svg",
    "text":      """authors build cfg changelog changes clslog conf contribs
                    contributors copyright copyrights csv doc docx dot dotx
                    hgignore hgsubstate hgtags in ini install installation
                    license md odf odp ods odt pages pdf pps ppsx ppt pptx
                    readme rst rtf txt version xls xlsx xlt xltx yml""",
    "video":     "avi m4v mov mp4"
              }
FILE_TYPES = {k:tuple(v.split()) for k,v in FILE_TYPES.items()}

# dict of descriptions and icons for all file type groups
FILE_DESCS_ICONS = {
    "app":       ("Application",     "../FileUI"),
    "archive":   ("Archive",         "ionicons-filing-32"),
    "audio":     ("Audio File",      "ionicons-ios7-musical-notes-32"),
    "code":      ("Source Code",     "../FilePY"),
    "code_tags": ("Source Code",     "ionicons-code-32"),
    "data":      ("Data File",       "ionicons-social-buffer-32"),
    "file":      ("File",            "ionicons-document-32"),
    "folder":    ("Folder",          "ionicons-folder-32"),
    "font":      ("Font File",       "../fonts-selected"),
    "git":       ("None",            "ionicons-social-github-32"),
    "image":     ("Image File",      "ionicons-image-32"),
    "text":      ("Plain Text File", "ionicons-document-text-32"),
    "video":     ("Video File",      "ionicons-ios7-film-outline-32"),
                   }
FILE_DESCS_ICONS = {k:(d,ui.Image.named(i)) for k,(d,i)
                        in FILE_DESCS_ICONS.items()}

fileinfo = collections.namedtuple('fileinfo',
            'file_ext recognized_ext filetype filedesc icon')

def get_filetype(file_ext):
    for filetype, exts in FILE_TYPES.items():
        if file_ext in exts:
            return filetype
    return None

def get_file_info(filename):
    if not isinstance(filename, str):
        return fileinfo('', '', '', '', None)
    recognized_ext_and_type = ('', '')
    for ext in os.path.basename(filename.lower()).split("."):
        filetype = get_filetype(ext)
        if filetype:
            recognized_ext_and_type = (ext, filetype)
    recognized_ext, filetype = recognized_ext_and_type
    is_dir = os.path.isdir(filename)
    if not filetype:
        filetype = "folder" if is_dir else "file"
    desc, icon = FILE_DESCS_ICONS.get(filetype, ("", None))
    # apply special descriptions, icons only to certain folders
    if is_dir and filetype not in ("app", "bundle", "git"):
        desc, folder_icon = FILE_DESCS_ICONS["folder"]
        if filetype != "archive":
            icon = folder_icon
    return fileinfo(ext, recognized_ext, filetype, desc, icon)

def get_thumbnail(path):
    def path_to_thumbnail(path):
        thumb = Image.open(path)
        thumb.thumbnail((32, 32), Image.ANTIALIAS)
        strio = io.StringIO()
        thumb.save(strio, thumb.format)
        data = strio.getvalue()
        strio.close()
        return ui.Image.from_data(data)

    try:  # attempt to generate a thumbnail
        return path_to_thumbnail(path)
    except IOError as err:
        if not err.message == "broken data stream when reading image file":
            return None
        tmp_file = os.path.join(SCRIPT_ROOT, "temp/filenav-tmp.png")
        # write image as png using ui module
        with open(tmp_file, "wb") as f:
            f.write(ui.Image.named(path).to_png())
        return path_to_thumbnail(tmp_file)

class FileItem(object):
    # object representation of a file and its properties
    def __init__(self, path):
        # init
        self.path = path
        self.refresh()

    def refresh(self):
        # refresh all properties
        self.path = full_path(self.path)
        self.fileinfo = get_file_info(self.path)
        self.icon = self.fileinfo.icon
        self.icon_cached = False
        self.rel_to_docs = rel_to_docs(self.path)
        self.location, self.name = os.path.split(self.path)
        try:
            self.stat = os.stat(self.path)
        except OSError as err:
            self.stat = err

        if os.path.isdir(self.path):
            self.basetype = 0
            try:
                self.contents = os.listdir(self.path)
            except OSError as err:
                self.contents = err
        else:
            self.basetype = 1
            self.contents = []

    def __del__(self):
        del self.path
        del self.fileinfo
        del self.icon
        del self.rel_to_docs
        del self.location
        del self.name
        del self.stat
        del self.contents

    def __repr__(self):
        # repr(self) and str(self)
        return "filenav.FileItem(" + self.path + ")"

    def __eq__(self, other):
        # self == other
        return os.path.samefile(self.path, other.path) if isinstance(other, FileItem) else False

    def __ne__(self, other):
        # self != other
        return not os.path.samefile(self.path, other.path) if isinstance(other, FileItem) else False

    def __len__(self):
        # len(self)
        return len(self.contents)

    def __getitem__(self, key):
        # self[key]
        return self.contents[key]

    def __iter__(self):
        # iter(self)
        return iter(self.contents)

    def __reversed__(self):
        # reversed(self)
        return reversed(self.contents)

    def __contains__(self, item):
        # item in self
        return item in self.contents

    def isdir(self):
        # like os.path.isdir
        return self.basetype == 0

    def isfile(self):
        # like os.path.isfile
        return self.basetype == 1

    def basename(self):
        # like os.path.basename
        return self.name

    def dirname(self):
        # like os.path.dirname
        return self.location

    def join(self, *args):
        # like os.path.join
        return os.path.join(self.path, *args)

    def listdir(self):
        # like os.listdir
        if self.isdir():
            return self.contents
        else:
            err = OSError()
            err.errno = errno.ENOTDIR
            err.strerror = os.strerror(err.errno)
            err.filename = self.path
            raise err

    def samefile(self, other):
        # like os.path.samefile
        return os.path.samefile(self.path, other)

    def split(self):
        # like os.path.split
        return (self.location, self.name)

    def as_cell(self):
        # Create a ui.TableViewCell for use with FileDataSource
        cell = ui.TableViewCell("subtitle")
        cell.text_label.text = self.name
        if not self.icon_cached and self.fileinfo.filetype == 'image':
            try:
                thumb = get_thumbnail(self.path)
            except:
                thumb = False
            if thumb:  # just-in-time creation of thumbnails
                self.icon = thumb
                self.icon_cached = True
        cell.image_view.image = self.icon
        cell.detail_text_label.text = FILE_EXTS.get(self.fileinfo.file_ext,
                                                    self.fileinfo.filedesc)
        if not isinstance(self.stat, OSError):  # if available, add size to subtitle
            cell.detail_text_label.text += " (" + format_size(self.stat.st_size, False) + ")"
        cell.accessory_type = "detail_{}button".format("disclosure_" if self.isdir() else "")
        return cell

CWD_FILE_ITEM = FileItem(os.getcwd())

class FileDataSource(object):
    # ui.TableView data source that generates a directory listing
    def __init__(self, fi=CWD_FILE_ITEM):
        # init
        self.fi = fi
        self.refresh()
        self.lists = [self.folders, self.files]

    def refresh(self):
        # Refresh the list of files and folders
        self.folders = []
        self.files = []
        for i in range(len(self.fi.contents)):
            if not isinstance(self.fi.contents[i], FileItem):
                # if it isn't already, make entries FileItems rather than strings
                self.fi.contents[i] = FileItem(self.fi.join(self.fi.contents[i]))

            if self.fi.contents[i].isdir():
                self.folders.append(self.fi.contents[i])
            else:
                self.files.append(self.fi.contents[i])

    def tableview_number_of_sections(self, tableview):
        # Return the number of sections
        return len(self.lists)

    def tableview_number_of_rows(self, tableview, section):
        # Return the number of rows in the section
        return len(self.lists[section])

    def tableview_cell_for_row(self, tableview, section, row):
        # Create and return a cell for the given section/row
        return self.lists[section][row].as_cell()

    def tableview_title_for_header(self, tableview, section):
        # Return a title for the given section.
        if section == 0:
            return "Folders"
        elif section == 1:
            return "Files"
        else:
            return "errsec"

    def tableview_can_delete(self, tableview, section, row):
        # Return True if the user should be able to delete the given row.
        return False

    def tableview_can_move(self, tableview, section, row):
        # Return True if a reordering control should be shown for the given row (in editing mode).
        return False

    def tableview_delete(self, tableview, section, row):
        # Called when the user confirms deletion of the given row.
        pass

    def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
        # Called when the user moves a row with the reordering control (in editing mode).
        pass

    @ui.in_background
    def tableview_did_select(self, tableview, section, row):
        # Called when the user selects a row
        if not tableview.editing:
            fi = self.lists[section][row]
            if section == 0:
                console.show_activity()
                nav.push_view(make_file_list(fi))
                console.hide_activity()
            elif section == 1:
                filetype = fi.fileinfo.filetype
                if fi.fileinfo.file_ext in ("htm", "html"):
                    webbrowser.open("file://" + fi.path)
                    nav.close()
                elif filetype in ("code", "code_tags", "text"):
                    open_path(fi.path)
                    nav.close()
                elif filetype == "audio":
                    spath = rel_to_app(fi.path.rsplit(".", 1)[0])
                    sound.load_effect(spath)
                    sound.play_effect(spath)
                elif filetype == "image":
                    console.show_image(fi.path)
                else:
                    console.quicklook(fi.path)
                    nav.close()

    def tableview_accessory_button_tapped(self, tableview, section, row):
        # Called when the user taps a row's accessory (i) button
        nav.push_view(make_stat_view(self.lists[section][row]))

class StatDataSource(object):
    # ui.TableView data source that shows os.stat() data on a file
    def __init__(self, fi=CWD_FILE_ITEM):
        # init
        self.fi = fi
        self.refresh()
        self.lists = [("Actions", self.actions), ("Stats", self.stats), ("Flags", self.flags)]

    def refresh(self):
        # Refresh stat data
        stres = self.fi.stat
        flint = stres.st_mode

        self.actions = []
        self.stats = (
            ("stat-size", "Size", format_size(stres.st_size), "ionicons-code-working-32"),
            ("stat-ctime", "Created", format_utc(stres.st_ctime), "ionicons-document-32"),
            ("stat-atime", "Opened", format_utc(stres.st_atime), "ionicons-folder-32"),
            ("stat-mtime", "Modified", format_utc(stres.st_mtime), "ionicons-ios7-compose-32"),
            ("stat-uid", "Owner", "{udesc} ({uid}={uname})".format(uid=stres.st_uid, uname=pwd.getpwuid(stres.st_uid)[0], udesc=pwd.getpwuid(stres.st_uid)[4]), "ionicons-ios7-person-32"),
            ("stat-gid", "Owner Group", str(stres.st_gid), "ionicons-ios7-people-32"),
            ("stat-flags", "Flags", str(bin(stres.st_mode)), "ionicons-ios7-flag-32"),
                     )
        self.flags = (
            ("flag-socket", "Is Socket", str(stat.S_ISSOCK(flint)), "ionicons-ios7-flag-32"),
            ("flag-link", "Is Symlink", str(stat.S_ISLNK(flint)), "ionicons-ios7-flag-32"),
            ("flag-reg", "Is File", str(stat.S_ISREG(flint)), "ionicons-ios7-flag-32"),
            ("flag-block", "Is Block Dev.", str(stat.S_ISBLK(flint)), "ionicons-ios7-flag-32"),
            ("flag-dir", "Is Directory", str(stat.S_ISDIR(flint)), "ionicons-ios7-flag-32"),
            ("flag-char", "Is Char Dev.", str(stat.S_ISCHR(flint)), "ionicons-ios7-flag-32"),
            ("flag-fifo", "Is FIFO", str(stat.S_ISFIFO(flint)), "ionicons-ios7-flag-32"),
            ("flag-suid", "Set UID Bit", str(check_bit(flint, stat.S_ISUID)), "ionicons-ios7-flag-32"),
            ("flag-sgid", "Set GID Bit", str(check_bit(flint, stat.S_ISGID)), "ionicons-ios7-flag-32"),
            ("flag-sticky", "Sticky Bit", str(check_bit(flint, stat.S_ISVTX)), "ionicons-ios7-flag-32"),
            ("flag-uread", "Owner Read", str(check_bit(flint, stat.S_IRUSR)), "ionicons-ios7-flag-32"),
            ("flag-uwrite", "Owner Write", str(check_bit(flint, stat.S_IWUSR)), "ionicons-ios7-flag-32"),
            ("flag-uexec", "Owner Exec", str(check_bit(flint, stat.S_IXUSR)), "ionicons-ios7-flag-32"),
            ("flag-gread", "Group Read", str(check_bit(flint, stat.S_IRGRP)), "ionicons-ios7-flag-32"),
            ("flag-gwrite", "Group Write", str(check_bit(flint, stat.S_IWGRP)), "ionicons-ios7-flag-32"),
            ("flag-gexec", "Group Exec", str(check_bit(flint, stat.S_IXGRP)), "ionicons-ios7-flag-32"),
            ("flag-oread", "Others Read", str(check_bit(flint, stat.S_IROTH)), "ionicons-ios7-flag-32"),
            ("flag-owrite", "Others Write", str(check_bit(flint, stat.S_IWOTH)), "ionicons-ios7-flag-32"),
            ("flag-oexec", "Others Exec", str(check_bit(flint, stat.S_IXOTH)), "ionicons-ios7-flag-32"),
                     )

        if self.fi.isdir():
            # actions for folders
            self.actions += [
                ("shellista-cd", "Go here", "Shellista", "ionicons-ios7-arrow-forward-32"),
                            ]
        elif self.fi.isfile():
            # actions for files
            self.actions += [
                ("ios-qlook", "Preview", "Quick Look", "ionicons-ios7-eye-32"),
                ("pysta-edit", "Open in Editor", "Pythonista", "ionicons-ios7-compose-32"),
                ("pysta-cpedit", "Copy & Open", "Pythonista", "ionicons-ios7-copy-32"),
                ("pysta-cptxt", "Copy & Open as Text", "Pythonista", "ionicons-document-text-32"),
                # haven't yet been able to integrate hexviewer
                #("hexviewer-open", "Open in Hex Viewer", "hexviewer", "ionicons-pound-32"),
                ("ios-openin", "Open In and Share", "External Apps", "ionicons-ios7-paperplane-32"),
                            ]
            if self.fi.fileinfo.file_ext in ("htm", "html"):
                self.actions[-1:-1] = [
                    ("webbrowser-open", "Open Website", "webbrowser", "ionicons-ios7-world-32")]
            elif self.fi.fileinfo.filetype == "image":
                self.actions[-1:-1] = [
                    ("console-printimg", "Show in Console", "console", "ionicons-image-32")]
            elif self.fi.fileinfo.filetype == "audio":
                self.actions[-1:-1] = [
                    ("sound-playsound", "Play Sound", "sound", "ionicons-ios7-play-32")]


    def tableview_number_of_sections(self, tableview):
        # Return the number of sections
        return len(self.lists)

    def tableview_number_of_rows(self, tableview, section):
        # Return the number of rows in the section
        return len(self.lists[section][1])

    def tableview_cell_for_row(self, tableview, section, row):
        # Create and return a cell for the given section/row
        if section == 0:
            cell = ui.TableViewCell("subtitle")
            cell.image_view.image = ui.Image.named(self.lists[section][1][row][3])
        else:
            cell = ui.TableViewCell("value2")
        cell.text_label.text = self.lists[section][1][row][1]
        cell.detail_text_label.text = self.lists[section][1][row][2]
        return cell

    def tableview_title_for_header(self, tableview, section):
        # Return a title for the given section.
        return self.lists[section][0]

    def tableview_can_delete(self, tableview, section, row):
        # Return True if the user should be able to delete the given row.
        return False

    def tableview_can_move(self, tableview, section, row):
        # Return True if a reordering control should be shown for the given row (in editing mode).
        return False

    def tableview_delete(self, tableview, section, row):
        # Called when the user confirms deletion of the given row.
        pass

    def tableview_move_row(self, tableview, from_section, from_row, to_section, to_row):
        # Called when the user moves a row with the reordering control (in editing mode).
        pass

    @ui.in_background # necessary to avoid hangs with Shellista and console modules
    def tableview_did_select(self, tableview, section, row):
        # Called when the user selects a row
        key = self.lists[section][1][row][0]
        if key == "shellista-cd":
            # Go Here - Shellista
            nav.close()
            print("Launching Shellista...")
            try:
                pipTerm = pipTerminal()
            except ImportError as err:
                print(("Failed to import Shellista: " + err.message))
                print("See note on Shellista integration at the top of filenav.py.")
                print("> logout")
                return
            pipTerm.main(cmd='cd {}'.format(self.fi.path))
        elif key == "ios-qlook":
            # Preview - Quick Look
            nav.close()
            time.sleep(1) # ui thread will hang otherwise
            console.quicklook(self.fi.path)
        elif key == "pysta-edit":
            # Open in Editor - Pythonista
            open_path(self.fi.path)
            nav.close()
        elif key == "pysta-cpedit":
            # Copy & Open - Pythonista
            destdir = full_path(os.path.join(SCRIPT_ROOT, "temp"))
            if not os.path.exists(destdir):
                os.mkdir(destdir)
            destfile = full_path(os.path.join(destdir, self.fi.basename().lstrip(".")))
            shutil.copy(self.fi.path, destfile)
            editor.reload_files()
            open_path(destfile)
            nav.close()
        elif key == "pysta-cptxt":
            # Copy & Open as Text - Pythonista
            destdir = full_path(os.path.join(SCRIPT_ROOT, "temp"))
            if not os.path.exists(destdir):
                os.mkdir(destdir)
            destfile = full_path(os.path.join(destdir, self.fi.basename().lstrip(".") + ".txt"))
            shutil.copy(self.fi.path, destfile)
            editor.reload_files()
            open_path(destfile)
            nav.close()
        elif key == "console-printimg":
            # Show in Console - console
            console.show_image(self.fi.path)
        elif key == "sound-playsound":
            # Play Sound - sound
            spath = rel_to_app(self.fi.path.rsplit(".", 1)[0])
            sound.load_effect(spath)
            sound.play_effect(spath)
        elif key == "webbrowser-open":
            # Open Website - webbrowser
            webbrowser.open("file://" + self.fi.path)
            nav.close()
        elif key == "ios-openin":
            # Open In - External Apps
            if console.open_in(self.fi.path):
                nav.close()
            else:
                console.hud_alert("Failed to Open", "error")

    def tableview_accessory_button_tapped(self, tableview, section, row):
        # Called when the user taps a row's accessory (i) button
        pass

def check_bit(num, bit):
    # Check if bit is set in num
    return (num ^ bit) < num

def format_size(size, long=True):
    if size < 1024:
        return str(int(size)) + " bytes"
    else:
        size, bsize = float(size), int(size)
        i = 0
        while size >= 1024.0 and i < len(SIZE_SUFFIXES)-1:
            size = size/1024.0
            i += 1
        if int:
            return "{size:02.2f} {suffix} ({bsize} bytes)".format(size=size, suffix=SIZE_SUFFIXES[i], bsize=bsize)
        else:
            return "{size:01.1f} {suffix}".format(size=size, suffix=SIZE_SUFFIXES[i])

def format_utc(timestamp):
    return str(datetime.datetime.fromtimestamp(timestamp)) + " UTC"

def open_path(path):
    # Open an absolute path in editor
    editor.open_file(os.path.relpath(path, os.path.expanduser("~/Documents")))

def toggle_edit_proxy(parent):
    # Returns a function that toggles edit mode for parent
    def _toggle_edit(sender):
        sender.title = "Edit" if parent.editing else "Done"
        parent.set_editing(not parent.editing)
    return _toggle_edit

def close_proxy():
    # Returns a function that closes the main view
    def _close(sender):
        nav.close()
    return _close

def make_file_list(fi=CWD_FILE_ITEM):
    # Create a ui.TableView containing a directory listing of path
    lst = ui.TableView(flex="WH")
    # allow multiple selection when editing, single selection otherwise
    lst.allows_selection = True
    lst.allows_multiple_selection = False
    lst.allows_selection_during_editing = True
    lst.allows_multiple_selection_during_editing = True
    lst.background_color = 1.0
    lst.data_source = lst.delegate = FileDataSource(fi)
    lst.name = "/" if fi.path == "/" else fi.basename()
    lst.right_button_items = ui.ButtonItem(title="Edit", action=toggle_edit_proxy(lst)),
    return lst

def make_stat_view(fi=CWD_FILE_ITEM):
    # Create a ui.TableView containing stat data on path
    lst = ui.TableView(flex="WH")
    # allow single selection only outside edit mode
    lst.allows_selection = True
    lst.allows_multiple_selection = False
    lst.allows_selection_during_editing = False
    lst.allows_multiple_selection_during_editing = False
    lst.background_color = 1.0
    lst.data_source = lst.delegate = StatDataSource(fi)
    lst.name = "/" if fi.path == "/" else fi.basename()
    return lst

def run(path="~", mode="popover"):
    # Run the main UI application
    global nav

    lst = make_file_list(CWD_FILE_ITEM if full_path(path) == "~" else FileItem(path))
    lst.left_button_items = ui.ButtonItem(image=ui.Image.named("ionicons-close-24"),
                                          action=close_proxy()),
    nav = ui.NavigationView(lst)
    nav.navigation_bar_hidden = False
    nav.flex = "WH"
    if mode == "popover":
        nav.height = 1000
    nav.present(mode, hide_title_bar=True)

BackupSTDOUT = sys.stdout
if __name__ == "__main__":
    try:
        run(sys.argv[1] if len(sys.argv) > 1 else "~")
    except:
        pass
sys.stdout = BackupSTDOUT
