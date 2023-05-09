#!python3

"""Pythonista3 Console Terminal"""

import code, console, os, re, shutil, socket, sys, urllib.request, time, tarfile, zipfile, urllib.parse, ssl, requests, signal
from console import set_color as setColor
from lib2to3.main import main as _2to3_main
from io import BytesIO
from platform import python_version
from platform import node as hostname
from urllib.error import URLError

ssl._create_default_https_context = ssl._create_unverified_context

Command_DIRNAME = ['{}@{}'.format(os.getenv('USER'), hostname()), '', '']
HOME_DIC = os.getcwd()
is_Exits = True
def Exit(arg=0):
    for _ in range(2):
        os.kill(os.getpid(), signal.SIGINT)

sys.exit = Exit
def _2to3(pyArgs):
    try:
        sys.argv[1:] = pyArgs
    except:
        pass
    try:
        _2to3_main('lib2to3.fixes')
    except:
        pass

def __init__():
    try:
        os.makedirs(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin'), exist_ok=True)
        default_bin = os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'bin')
        files = os.listdir(default_bin)
        for f in range(len(files)):
            shutil.move(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', 'bin', files[f]), os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin'))
    except:
        pass

def SystemLogo():
    clear()
    setColor(255, 0, 0) # red
    return "{}\n| - pyTerminal v2.0.6 on Python {}\t\t\t|\n| - Author: DarkRix.\t\t\t\t\t\t|\n| - Show All Command: help\t\t\t\t\t|\n{}\n\n".format("-"*41, python_version(), "-"*41)

def Argument_Paser(Args):
    setColor()
    try:
        try:
            if Args[1] == '-h' and Args[0] == 'cat':
                print("Usage: cat [-h] [files [files ...]]")
            if Args[1] == '-h' and Args[0] == 'cd':
                print("Usage: cd [-h] [dir]\n\nChange the Current working directory.")
            if Args[1] == '-h' and Args[0] == 'cp':
                print("Usage: cp [-h] source [source ...] dest")
            if Args[1] == '-h' and Args[0] == 'echo':
                print("Usage: echo [-h]\n\nPrint All arguments to stdout, separated by space")
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
            if Args[1] == '-h' and Args[0] == 'python3':
                print("Usage: python3 [-h] [file]\n\nPython Interactive Shell.")
            if Args[1] == '-h' and Args[0] == 'wget':
                print("Usage: wget [-h] [url]\n\nA simple File Download.")
            if Args[1] == '-h' and Args[0] == 'unzip':
                print('Usage: unzip [-h] [file]')
            if Args[1] == '-h' and Args[0] == 'zip':
                print('Usage: zip [-h] [OutPutFileName] [Target]')
        except IndexError:
            pass
        try:
            if Args[0] == 'help':
                print('[Default commands]:\nhelp, 2to3, cat, cd, echo, env, git(clone only), la, ls, ln, mkdir, open, ping, rm, tar, uznip, wget, zip, python, python3, exit\n\n[Third Party commands]:\n' + list_other_cmd() + '\n\n[Stash Extensions Commands]:\n' + list_stash_bin())
            elif Args[0] == 'cat':
                try:
                    if not Args[1] == '-h':
                        print(readfile(Args[1]))
                except:
                    pass
            elif Args[0] == '2to3':
                try:
                    _2to3(Args[1:])
                except:
                    pass
            elif Args[0] == 'cd':
                try:
                    if not Args[1] == '-h':
                        try:
                            try:
                                if Args[1][0] == '$':
                                    chdirs(os.getenv(Args[1][1:]))
                                else:
                                    chdirs(Args[1])
                            except IndexError:
                                chdirs(HOME_DIC)
                            if Args[1] == '':
                                chdirs(HOME_DIC)
                            if Args[1] == ' ':
                                chdirs(HOME_DIC)
                        except KeyboardInterrupt:
                            is_Exits = False
                            [os.kill(os.getpid(), signal.SIGINT) for _ in range(2)]
                            is_Exits = False
                        except:
                            pass
                except:
                    chdirs(HOME_DIC)
            elif Args[0] == 'cp':
                try:
                    if not '/' in Args[2]:
                        copyFiles(os.path.join(os.getcwd(),Args[1]),os.path.join(os.getcwd(), Args[2]))
                    else:
                        copyFiles(os.path.join(os.getcwd(),Args[1]), Args[2])
                except:
                    pass
            elif Args[0] == 'echo':
                try:
                    try:
                        if Args[0][4] == '>':
                            create_empty_file(Args[0][5:])
                        else:
                            pass
                    except IndexError:
                        pass
                    try:
                        if Args[1] == '>':
                            create_empty_file(Args[2])
                        if Args[1][0] == '$':
                            env_data = os.getenv(Args[1][1:])
                            if not env_data is None:
                                print(env_data)
                    except IndexError:
                        pass
                    try:
                        if not Args[1] == '' and Args[2][0] == '>':
                            create_file(Args[2][1:], Args[1])
                    except IndexError:
                        pass
                    try:
                        if not Args[1] == '' and Args[2] == '>':
                            create_file(Args[3], Args[1])
                    except IndexError:
                        try:
                            if not Args[1] == '':
                                print(Args[1])
                        except IndexError:
                            print()
                except:
                    pass
            elif Args[0] == 'env':
                for item, value in os.environ.items():
                    setColor(255, 0, 0)
                    print('{}'.format(item), end=': ')
                    setColor()
                    print(value)
            elif Args[0] == 'git':
                try:
                    if not Args[1] == '-h':
                        if Args[1] == 'clone':
                            git_clone(Args[2:])
                        else:
                            print('This git is clone command only')
                except IndexError:
                    print('Usage: git clone <url> [path] - clone a remote repository')
                except:
                    pass
            elif Args[0] == 'la':
                try:
                    try:
                        if Args[1] == '-l':
                            listdir('long', os.getcwd())
                    except IndexError:
                        listdir(None, None)
                except:
                    pass
            elif Args[0] == 'ls':
                try:
                    try:
                        if Args[1] == '-l':
                            listdir('long', os.getcwd())
                    except IndexError:
                        listdir(None, None)
                except:
                    pass
            elif Args[0] == 'ln':
                try:
                    if not Args[1] == '-h':
                        if Args[1] == '-s':
                            try:
                                if not '/' in Args[2] and not '/' in Args[3]:
                                    Symbolic_Link(os.path.join(os.getcwd(), Args[2]), os.path.join(os.getcwd(), Args[3]))
                                else:
                                    Symbolic_Link(Args[2], Args[3])
                            except:
                                pass
                        else:
                            try:
                                if not '/' in Args[1]:
                                    Symbolic_Link(os.path.join(os.getcwd(), Args[1]), Args[2])
                                else:
                                    Symbolic_Link(Args[1], Args[2])
                            except:
                                pass
                except:
                    pass
            elif Args[0] == 'mkdir':
                try:
                    if not Args[1] == '-h':
                        if Args[1] == '-p':
                            os.makedirs(Args[2], exist_ok=True)
                        else:
                            os.makedirs(Args[1], exist_ok=True)
                except:
                    pass
            elif Args[0] == 'mv':
                try:
                    if not Args[1] == '-h':
                        try:
                            shutil.move(Args[1], Args[2])
                        except IndexError:
                            pass
                        except Exception as Err:
                            print(Err)
                except:
                    pass
            elif Args[0] == 'open':
                try:
                    console.quicklook(Args[1])
                except Exception as E:
                    print(E)
            elif Args[0] == 'ping':
                try:
                    if not Args[1] == '-h':
                        if Args[1] == '-c':
                            try:
                                for _G in range(int(Args[2])):
                                    print(ping(Args[3]))
                                    time.sleep(1)
                            except IndexError:
                                pass
                        else:
                            if Args[1] == '':
                                pass
                            else:
                                for _P in range(3):
                                    print(ping(Args[1]))
                                    time.sleep(1)
                except:
                    pass
            elif Args[0] == 'pwd':
                try:
                    try:
                        PWD = os.getcwd()
                    except Exception as PWDErr:
                        PWD = PWDErr
                    print(PWD)
                except:
                    pass
            elif Args[0] == 'rm':
                try:
                    if not Args[1] == '-h':
                        if Args[1][0:] == './':
                            try:
                                for _rm in range(len(os.listdir())):
                                    delete_Files(os.listdir()[_rm])
                            except:
                                try:
                                    for _rm in range(len(os.listdir())):
                                        delete_Files(os.listdir()[_rm])
                                except:
                                    pass
                        else:
                            delete_Files(Args[1])
                except IndexError:
                    try:
                        delete_Files(Args[1])
                    except Exception as Err:
                        print(Err)
                except:
                    pass
            elif Args[0] == 'tar':
                TarArgument(Args)
            elif Args[0] == 'unzip':
                try:
                    if not Args[1] == '-h':
                        ZIPExtractor(Args[1])
                except IndexError:
                    pass
                except:
                    pass
            elif Args[0] == 'python':
                try:
                    if not Args[1] == '-h':
                        try:
                            if not '/' in Args[1]:
                                file_path = os.path.join(os.getcwd(), Args[1])
                            else:
                                file_path = Args[1]
                            py_file = open(file_path, 'r', encoding='utf-8').read()
                            try:
                                exec(py_file)
                            except SystemExit:
                                pass
                            except:
                                pass
                        except:
                            try:
                                code.interact()
                            except SystemExit:
                                pass
                except:
                    pass
            elif Args[0] == 'python3':
                try:
                    if not Args[1] == '-h':
                        try:
                            if not '/' in Args[1]:
                                file_path = os.path.join(os.getcwd(), Args[1])
                            else:
                                file_path = Args[1]
                            py_file = open(file_path, 'r', encoding='utf-8').read()
                            try:
                                exec(py_file)
                            except:
                                pass
                        except:
                            try:
                                code.interact()
                            except SystemExit:
                                pass
                except:
                    pass
            elif Args[0] == 'wget':
                try:
                    if not Args[1] == '-h':
                        try:
                            if Args[2] == '-o':
                                wget(Args[1], filename=Args[3])
                            elif Args[2] == '--output':
                                wget(Args[1], filename=Args[3])
                        except IndexError:
                            wget(Args[1])
                except KeyboardInterrupt:
                    is_Exits = False
                    [os.kill(os.getpid(), signal.SIGINT) for _ in range(2)]
                    is_Exits = False
                    print(end='\r')
                except:
                    pass
            elif Args[0] == 'zip':
                try:
                    if not Args[1] == '-h':
                        ZipArchiveCreate(Args[1], Args[2])
                except IndexError:
                    pass
                except:
                    pass
            elif Args[0] == 'exit':
                print('Exiting.......')
                is_Exits = False
                [os.kill(os.getpid(), signal.SIGINT) for _ in range(2)]
                is_Exits = False
            elif Args[0] == 'clear':
                clear()
            elif Args[0] == 'cls':
                clear()
            elif Args[0] == '':
                pass
            elif Args[0] == ' ':
                pass
            else:
                run_other_cmd(Args[0], Args[1:])
        except KeyboardInterrupt:
            sys.exit(0)
            clear()
    except KeyboardInterrupt:
        sys.exit(0)
        clear()

def clear():
    console.clear()

def chdirs(Location):
    try:
        os.chdir(Location)
    except Exception as E:
        print('ERROR:{}'.format(E))

def create_empty_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('')

def create_file(Fname, Data):
    with open(Fname, 'w', encoding='utf-8') as f:
        f.write(Data)

def copyFiles(FileName, dest):
    try:
        if os.path.isfile(os.path.join(os.getcwd(), FileName)):
            shutil.copy(FileName, dest)
        elif os.path.isdir(os.path.join(os.getcwd(), FileName)):
            shutil.copytree(FileName, dest)
    except Exception as e:
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
    elif os.path.isdir(os.path.join(os.getcwd(), file)):
        setColor()
        setColor(0, 0, 205)
        return file
    else:
        setColor()
        return file

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

def git_clone(gitArgs):
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
        except URLError:
            reURL = 'https://github.com/{}/{}'.format(UserName, ProjectName)
            FFdata = urllib.request.urlopen(urllib.request.Request(reURL, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; en-la) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 YJApp-ANDROID jp.co.yahoo.android.yjtop/13.91.1','Connection': 'keep-alive','Accept-Encoding': 'identity'})).read()
            Pattern = '{}/{}/tree/(.*?)/'.format(UserName, ProjectName)
            master_name = re.findall(Pattern, str(FFdata))[-1]
            ffURL = 'https://codeload.github.com/{}/{}/zip/{}'.format(UserName, ProjectName, master_name)
            RESPONSE_DATA = urllib.request.urlopen(urllib.request.Request(ffURL, headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; en-la) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 YJApp-ANDROID jp.co.yahoo.android.yjtop/13.91.1','Connection': 'keep-alive','Accept-Encoding': 'identity', 'HOSTS': 'github.com'})).read()
        with zipfile.ZipFile(BytesIO(RESPONSE_DATA), 'r') as Fzip:
            Fzip.extractall(gitPATH+'/.')
        vName = gitFileName + '-' + master_name
        if os.path.exists(vName):
            os.rename(vName, gitFileName)
        print('Done')

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

def list_stash_bin():
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

def list_other_cmd():
    list = sorted(os.listdir(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin')))
    for d in range(len(list)):
        try:
            if os.path.isdir(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin', list[d])):
                del list[d]
        except:
            pass
    return ', '.join(list)

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

def readfile(Name):
    try:
        rfile = open(Name, 'r', encoding='utf-8').read()
        return rfile
    except:
        pass

def run_stash_bin(cmdName, Sargs):
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

def run_other_cmd(cmd_name, args):
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
        run_stash_bin(cmd_name, args)
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

def wget(URL, filename=''):
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

def help_tar():
    print('tar [-h] [-j] [-z] [-x] [file [files ...]]')
    print('Support Archive Type: tar.gz or tar.')
    print('This command is extract only.')

def TarArgument(ARGS):
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
            help_tar()
        elif 'h' in ARGS[1][1:]:
            help_tar()
        else:
            help_tar()
    except IndexError:
        help_tar()
    except KeyboardInterrupt:
        sys.exit(0)
        clear()
    except:
        pass

def ExtractMems(mem, ext):
    for tf in mem:
        for pt in ext:
            if tf.name == pt or tf.name.startswith(pt):
                yield tf

def tExtract_ALL(FName, tArgs, mems=None, Dir='./'):
    if 'z' in tArgs[0]:
        print('Reading gzip file')
        tar = tarfile.open(FName, 'r:gz')
    elif 'j' in tArgs[0]:
        print('Reading bz2 file')
        tar = tarfile.open(FName, 'r:bz2')
    if mems:
        tar.extractall(path=Dir, members=ExtractMems(tar, mems))
    else:
        tar.extractall(path=Dir)
    tar.close()
    print('Archive Extracted')

def ZIPExtractor(zFileName):
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

def ZipArchiveCreate(ziPFilename, IPath):
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

def main():
    __init__()
    print(SystemLogo())
    setColor()
    while is_Exits:
        try:
            setColor(0, 102, 0)
            Command_DIRNAME[2] = ''
            print(Command_DIRNAME[0], end='\r', flush=True)
            setColor()
            print(':', end='', flush=True)
            setColor(0, 10, 255)
            try:
                Command_DIRNAME[2] = os.getcwd().replace(os.getenv('HOME'), '~')
            except Exception as Err:
               print(Err)
               try:
                   Argument_Paser(['cd', '../'])
               except:
                  print('Occurred Some Errors,\nExiting.........')
                  sys.exit(0)
                  clear()
            print(Command_DIRNAME[2], end='', flush=True)
            setColor()
            INPUT_Argument = input('$ ').split(' ')
            Argument_Paser(INPUT_Argument)
        except KeyboardInterrupt:
            sys.exit(0)
            clear()
        if not is_Exits:
            break
    clear()

if __name__ == '__main__':
    main()
