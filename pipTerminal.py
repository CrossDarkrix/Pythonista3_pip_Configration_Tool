#!python3

"""
Pythonista3 Console Terminal
"""

import code, console, os, requests, shutil, socket, sys, time
from console import set_color as setColor
from six.moves.urllib.request import urlopen

HOME_DIC = os.getcwd()

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
    return "- pyTerminal v1.5 on Python3.6.3\n- Author: DarkRix.\n\n- Show All Commands: help\n"

def Argument_Paser(Args):
    try:
        try:
            if Args[1] == '-h' and Args[0] == 'cat':
                print("Usage: cat [-h] [files [files ...]]")
                PASS()
            if Args[1] == '-h' and Args[0] == 'cd':
                print("Usage: cd [-h] [dir]\n\nChange the Current working directory.")
                PASS()
            if Args[1] == '-h' and Args[0] == 'cp':
                print("Usage: cp [-h] source [source ...] dest")
                PASS()
            if Args[1] == '-h' and Args[0] == 'echo':
                print("Usage: echo [-h]\n\nPrint All arguments to stdout, separated by space")
                PASS()
            if Args[1] == '-h' and Args[0] == 'la':
                print("Usage: la [-h] [-l] [files [files ...]]")
                PASS()
            if Args[1] == '-h' and Args[0] == 'ls':
                print("Usage: ls [-h] [-l] [files [files ...]]")
                PASS()
            if Args[1] == '-h' and Args[0] == 'ln':
                print("Usage: ln [-h] lhs rhs\n\nCreate Symblic Link.")
                PASS()
            if Args[1] == '-h' and Args[0] == 'mkdir':
                print("Usage: mkdir [-h] [-p] dir [dir ...]\n\nCreate a new directory.\nThe parent directory must specified.")
                PASS()
            if Args[1] == '-h' and Args[0] == 'mv':
                print("Usage: mv [-h] src [src ...] dest\n\nMove(Rename) a file or directory to a new name, or into a new directory.")
                PASS()
            if Args[1] == '-h' and Args[0] == 'ping':
                print("Usage: ping [-h] [-c COUNT] Destination\n\nSend ICMP ECHO_REQUET to network hosts.")
                PASS()
            if Args[1] == '-h' and Args[0] == 'rm':
                print("Usage: rm [-h] paths [paths ...]")
                PASS()
            if Args[1] == '-h' and Args[0] == 'touch':
                print("Usage: touch [-h] file [file ...]\n\nUpdate the modification time of the given files, and create them if they do not yet exist.")
                PASS()
            if Args[1] == '-h' and Args[0] == 'python':
                print("Usage: python [-h] [file]\n\nPython Interactive Shell.")
                PASS()
            if Args[1] == '-h' and Args[0] == 'python3':
                print("Usage: python3 [-h] [file]\n\nPython Interactive Shell.")
                PASS()
            if Args[1] == '-h' and Args[0] == 'wget':
                print("Usage: wget [-h] [url]\n\nA simple File Download.")
                PASS()
        except IndexError:
            pass
        except KeyboardInterrupt:
            sys.exit(0)
        try:
            if Args[0] == 'help':
                print('[Default commands]:\nhelp, cat, cd, echo, env, la, ls, ln, mkdir, ping, rm, wget, python, python3, exit\n\n[Third Party commands]:\n' + list_other_cmd())
            elif Args[0] == 'cat':
                try:
                    if not Args[1] == '-h':
                        print(readfile(Args[1]))
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            elif Args[0] == 'cd':
                try:
                    if not Args[1] == '-h':
                        try:
                            try:
                                if Args[1][1:] == '$':
                                    chdirs(os.getenv(Args.replace('$', '')))
                                else:
                                    chdirs(Args[1])
                            except IndexError:
                                chdirs(HOME_DIC)
                            if Args[1] == '':
                                chdirs(HOME_DIC)
                            if Args[1] == ' ':
                                chdirs(HOME_DIC)
                        except KeyboardInterrupt:
                            sys.exit(0)
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
                except KeyboardInterrupt:
                    sys.exit(0)
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
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            elif Args[0] == 'env':
                print('\n'.join('{item}: {value}'.format(item=i, value=v) for i, v in os.environ.items()))
            elif Args[0] == 'la':
                try:
                    try:
                        if Args[1] == '-l':
                            listdir('long', os.getcwd())
                    except IndexError:
                        listdir(None, None)
                    except KeyboardInterrupt:
                        sys.exit(0)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            elif Args[0] == 'ls':
                try:
                    try:
                        if Args[1] == '-l':
                            listdir('long', os.getcwd())
                    except IndexError:
                        listdir(None, None)
                    except KeyboardInterrupt:
                        sys.exit(0)
                except KeyboardInterrupt:
                    sys.exit(0)
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
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            elif Args[0] == 'mkdir':
                try:
                    if not Args[1] == '-h':
                        if Args[1] == '-p':
                            os.makedirs(Args[2], exist_ok=True)
                        else:
                            os.makedirs(Args[1], exist_ok=True)
                except KeyboardInterrupt:
                    sys.exit(0)
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
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
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
                except KeyboardInterrupt:
                    sys.exit(0)
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
                    except Exception as E:
                        print(E)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            elif Args[0] == 'touch':
                try:
                    if not Args[1] == '-h':
                        create_empty_file(Args[1])
                except KeyboardInterrupt:
                    sys.exit(0)
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
                            try:
                                code.interact()
                            except SystemExit:
                                pass
                except KeyboardInterrupt:
                    sys.exit(0)
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
                            except SystemExit:
                                pass
                        except:
                            try:
                                code.interact()
                            except SystemExit:
                                pass
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            elif Args[0] == 'wget':
                try:
                    if not Args[1] == '-h':
                        wget(Args[1])
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            elif Args[0] == 'exit':
                print('Exiting.......')
                sys.exit(0)
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
    except KeyboardInterrupt:
        sys.exit(0)

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
    list = sorted(os.listdir(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin')))
    for d in range(len(list)):
        try:
            if os.path.isdir(os.path.join(os.getenv('HOME'), 'Documents', 'site-packages', '_bin', list[d])):
                del list[d]
        except:
            pass
    return ', '.join(list)

def PASS():
    pass

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

def StartUP():
    __init__()
    print(SystemLogo())
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)

def main():
    setColor()
    try:
        while True:
            try:
                INPUT_Argument = input('Pythonista3:~# ').split(' ')
                Argument_Paser(INPUT_Argument)
            except KeyboardInterrupt:
                sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    StartUP()