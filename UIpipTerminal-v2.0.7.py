#!python3

"""Pythonista3 Ui Terminal"""

import base64, code, console, os, re, shutil, socket, sys, urllib.request, ui, time, tarfile, zipfile, urllib.parse, ssl, requests
from console import set_color as setColor
from lib2to3.main import main as _2to3_main
from io import BytesIO
from platform import python_version
from platform import node as hostname
from urllib.error import URLError

ssl._create_default_https_context = ssl._create_unverified_context

HOME_DIC = os.getcwd()

def SheetStr():
    return base64.b64decode('WwogIHsKICAgICJub2RlcyIgOiBbCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3sxMiwgMzJ9LCB7NjIsIDQ1fX0iLAogICAgICAgICJjbGFzcyIgOiAiTGFiZWwiLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJuYW1lIiA6ICIiLAogICAgICAgICAgInRleHRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wODMzMzMsMC4wODMzMzMsMS4wMDAwMDApIiwKICAgICAgICAgICJmcmFtZSIgOiAie3sxMTAsIDI3MH0sIHsxNTAsIDMyfX0iLAogICAgICAgICAgInV1aWQiIDogIjk5NUNEMTgzLTc5MTYtNDUyOC04OUExLThERDM0NjY3QjQ2QSIsCiAgICAgICAgICAiY2xhc3MiIDogIkxhYmVsIiwKICAgICAgICAgICJhbGlnbm1lbnQiIDogImxlZnQiLAogICAgICAgICAgInRleHQiIDogIlB5Mzp+IyIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDE4LAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbT4iCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezEyLCAyMTh9LCB7MzU4LCAzNDd9fSIsCiAgICAgICAgImNsYXNzIiA6ICJUZXh0VmlldyIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgInV1aWQiIDogIjYwNEIxNUU2LTNEOEUtNEI1RC1CMUI1LUQxNDI3OEQyNkE2NiIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDE3LAogICAgICAgICAgImZyYW1lIiA6ICJ7ezg1LCAxODZ9LCB7MjAwLCAyMDB9fSIsCiAgICAgICAgICAiZWRpdGFibGUiIDogZmFsc2UsCiAgICAgICAgICAiYWxpZ25tZW50IiA6ICJsZWZ0IiwKICAgICAgICAgICJhdXRvY29ycmVjdGlvbl90eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDAwMDAwLDAuMDAwMDAwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtPiIsCiAgICAgICAgICAic3BlbGxjaGVja2luZ190eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJjbGFzcyIgOiAiVGV4dFZpZXciLAogICAgICAgICAgIm5hbWUiIDogIlByaW50VGVybWluYWwiLAogICAgICAgICAgImZsZXgiIDogIldIIgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IGZhbHNlCiAgICAgIH0sCiAgICAgIHsKICAgICAgICAibm9kZXMiIDogWwoKICAgICAgICBdLAogICAgICAgICJmcmFtZSIgOiAie3s3MiwgMzJ9LCB7MjkyLCA0NX19IiwKICAgICAgICAiY2xhc3MiIDogIlRleHRGaWVsZCIsCiAgICAgICAgImF0dHJpYnV0ZXMiIDogewogICAgICAgICAgImFjdGlvbiIgOiAibWFpbiIsCiAgICAgICAgICAibmFtZSIgOiAiVGVybWluYWxDbWQiLAogICAgICAgICAgInRleHRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wMDAwMDAsMC4wMDAwMDAsMS4wMDAwMDApIiwKICAgICAgICAgICJmcmFtZSIgOiAie3s4NSwgMjcwfSwgezIwMCwgMzJ9fSIsCiAgICAgICAgICAic3BlbGxjaGVja2luZ190eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJjbGFzcyIgOiAiVGV4dEZpZWxkIiwKICAgICAgICAgICJ1dWlkIiA6ICJDMDYwMjJDRS0wRUQ1LTRGRjgtQjFFQS1FQ0U3MUJDMTc3NTAiLAogICAgICAgICAgImFsaWdubWVudCIgOiAibGVmdCIsCiAgICAgICAgICAiYXV0b2NvcnJlY3Rpb25fdHlwZSIgOiAiZGVmYXVsdCIsCiAgICAgICAgICAiZm9udF9zaXplIiA6IDE3LAogICAgICAgICAgImZvbnRfbmFtZSIgOiAiPFN5c3RlbT4iCiAgICAgICAgfSwKICAgICAgICAic2VsZWN0ZWQiIDogZmFsc2UKICAgICAgfSwKICAgICAgewogICAgICAgICJub2RlcyIgOiBbCgogICAgICAgIF0sCiAgICAgICAgImZyYW1lIiA6ICJ7ezYsIDg1fSwgezM1OCwgMTM0fX0iLAogICAgICAgICJjbGFzcyIgOiAiVGV4dFZpZXciLAogICAgICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgICAgICJ1dWlkIiA6ICJDQkE3Rjk1Qy1CRTU5LTQ4MjgtOUI4MS01NERDMjEwRDdFMDMiLAogICAgICAgICAgImZvbnRfc2l6ZSIgOiAxNywKICAgICAgICAgICJmcmFtZSIgOiAie3s4NSwgMTg2fSwgezIwMCwgMjAwfX0iLAogICAgICAgICAgImVkaXRhYmxlIiA6IGZhbHNlLAogICAgICAgICAgImFsaWdubWVudCIgOiAiY2VudGVyIiwKICAgICAgICAgICJhdXRvY29ycmVjdGlvbl90eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJ0ZXh0X2NvbG9yIiA6ICJSR0JBKDEuMDAwMDAwLDAuMDAwMDAwLDAuMDAwMDAwLDEuMDAwMDAwKSIsCiAgICAgICAgICAiZm9udF9uYW1lIiA6ICI8U3lzdGVtPiIsCiAgICAgICAgICAic3BlbGxjaGVja2luZ190eXBlIiA6ICJkZWZhdWx0IiwKICAgICAgICAgICJjbGFzcyIgOiAiVGV4dFZpZXciLAogICAgICAgICAgIm5hbWUiIDogIkxvZ28iLAogICAgICAgICAgImZsZXgiIDogIldIIgogICAgICAgIH0sCiAgICAgICAgInNlbGVjdGVkIiA6IHRydWUKICAgICAgfQogICAgXSwKICAgICJmcmFtZSIgOiAie3swLCAwfSwgezM3MCwgNTcxfX0iLAogICAgImNsYXNzIiA6ICJWaWV3IiwKICAgICJhdHRyaWJ1dGVzIiA6IHsKICAgICAgImJhY2tncm91bmRfY29sb3IiIDogIlJHQkEoMC4wODYxNDIsMC4wODYxNDIsMC4wODYxNDIsMS4wMDAwMDApIiwKICAgICAgImVuYWJsZWQiIDogdHJ1ZSwKICAgICAgInRpbnRfY29sb3IiIDogIlJHQkEoMS4wMDAwMDAsMC4wODMzMzMsMC4wODMzMzMsMS4wMDAwMDApIiwKICAgICAgIm5hbWUiIDogInBpcFRlcm1pbmFsIiwKICAgICAgImJvcmRlcl9jb2xvciIgOiAiUkdCQSgwLjAwMDAwMCwwLjAwMDAwMCwwLjAwMDAwMCwxLjAwMDAwMCkiLAogICAgICAiZmxleCIgOiAiIgogICAgfSwKICAgICJzZWxlY3RlZCIgOiBmYWxzZQogIH0KXQ==').decode()
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
    return "{}\n| - pyTerminal v2.0.7 on Python {}\t\t|\n| - Author: DarkRix.\t\t\t\t\t\t|\n| - Show All Command: help\t\t\t\t|\n{}\n\n".format("-"*41, python_version(), "-"*41)

def Argument_Paser(Args, send):
    setColor()
    try:
        try:
            if Args[1] == '-h' and Args[0] == 'cat':
                send.superview['PrintTerminal'].text = "Usage: cat [-h] [files [files ...]]"
            if Args[1] == '-h' and Args[0] == 'cd':
                send.superview['PrintTerminal'].text = "Usage: cd [-h] [dir]\n\nChange the Current working directory."
            if Args[1] == '-h' and Args[0] == 'cp':
                send.superview['PrintTerminal'].text = "Usage: cp [-h] source [source ...] dest"
            if Args[1] == '-h' and Args[0] == 'echo':
                send.superview['PrintTerminal'].text = "Usage: echo [-h]\n\nPrint All arguments to stdout, separated by space"
            if Args[1] == '-h' and Args[0] == 'git':
                send.superview['PrintTerminal'].text = 'Usage: git clone <url> [path] - clone a remote repository'
            if Args[1] == '-h' and Args[0] == 'la':
                send.superview['PrintTerminal'].text = "Usage: la [-h] [-l] [files [files ...]]"
            if Args[1] == '-h' and Args[0] == 'ls':
                send.superview['PrintTerminal'].text = "Usage: ls [-h] [-l] [files [files ...]]"
            if Args[1] == '-h' and Args[0] == 'ln':
                send.superview['PrintTerminal'].text = "Usage: ln [-h] lhs rhs\n\nCreate Symblic Link."
            if Args[1] == '-h' and Args[0] == 'mkdir':
                send.superview['PrintTerminal'].text = "Usage: mkdir [-h] [-p] dir [dir ...]\n\nCreate a new directory.\nThe parent directory must specified."
            if Args[1] == '-h' and Args[0] == 'mv':
                send.superview['PrintTerminal'].text = "Usage: mv [-h] src [src ...] dest\n\nMove(Rename) a file or directory to a new name, or into a new directory."
            if Args[1] == '-h' and Args[0] == 'ping':
                send.superview['PrintTerminal'].text = "Usage: ping [-h] [-c COUNT] Destination\n\nSend ping to network hosts."
            if Args[1] == '-h' and Args[0] == 'rm':
                send.superview['PrintTerminal'].text = "Usage: rm [-h] paths [paths ...]"
            if Args[1] == '-h' and Args[0] == 'python':
                send.superview['PrintTerminal'].text = "Usage: python [-h] [file]\n\nPython Interactive Shell."
            if Args[1] == '-h' and Args[0] == 'python3':
                send.superview['PrintTerminal'].text = "Usage: python3 [-h] [file]\n\nPython Interactive Shell."
            if Args[1] == '-h' and Args[0] == 'wget':
                send.superview['PrintTerminal'].text = "Usage: wget [-h] [url]\n\nA simple File Download."
            if Args[1] == '-h' and Args[0] == 'unzip':
                send.superview['PrintTerminal'].text = 'Usage: unzip [-h] [file]'
            if Args[1] == '-h' and Args[0] == 'zip':
                send.superview['PrintTerminal'].text = 'Usage: zip [-h] [OutPutFileName] [Target]'
        except IndexError:
            pass
        try:
            if Args[0] == 'help':
                send.superview['PrintTerminal'].text = '[Default commands]:\nhelp, 2to3, cat, cd, echo, env, git(clone only), la, ls, ln, mkdir, open, ping, rm, tar, uznip, wget, zip, python, python3, exit\n\n[Third Party commands]:\n' + list_other_cmd() + '\n\n[Stash Extensions Commands]:\n' + list_stash_bin()
            elif Args[0] == 'cat':
                try:
                    if not Args[1] == '-h':
                        send.superview['PrintTerminal'].text = readfile(Args[1])
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
                                    chdirs(os.getenv(Args[1][1:]), send)
                                else:
                                    chdirs(Args[1], send)
                            except IndexError:
                                chdirs(HOME_DIC, send)
                            if Args[1] == '':
                                chdirs(HOME_DIC, send)
                            if Args[1] == ' ':
                                chdirs(HOME_DIC, send)
                        except KeyboardInterrupt:
                            sys.exit(0)
                        except:
                            pass
                except:
                    chdirs(HOME_DIC, send)
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
                                send.superview['PrintTerminal'].text = env_data
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
                                send.superview['PrintTerminal'].text = Args[1]
                        except IndexError:
                            send.superview['PrintTerminal'].text = ''
                except:
                    pass
            elif Args[0] == 'env':
                for item, value in os.environ.items():
                    setColor(255, 0, 0)
                    send.superview['PrintTerminal'].text = '{}'.format(item)
                    setColor()
                    send.superview['PrintTerminal'].text = value
            elif Args[0] == 'git':
                try:
                    if not Args[1] == '-h':
                        if Args[1] == 'clone':
                            git_clone(Args[2:], send)
                        else:
                            send.superview['PrintTerminal'].text = 'This git is clone command only'
                except IndexError:
                    send.superview['PrintTerminal'].text = 'Usage: git clone <url> [path] - clone a remote repository'
                except:
                    pass
            elif Args[0] == 'la':
                try:
                    try:
                        if Args[1] == '-l':
                            listdir('long', os.getcwd(), send)
                    except IndexError:
                        listdir(None, None, send)
                    sys.exit(0)
                except:
                    pass
            elif Args[0] == 'ls':
                try:
                    try:
                        if Args[1] == '-l':
                            listdir('long', os.getcwd(), send)
                    except IndexError:
                        listdir(None, None, send)
                except:
                    pass
            elif Args[0] == 'ln':
                try:
                    if not Args[1] == '-h':
                        if Args[1] == '-s':
                            try:
                                if not '/' in Args[2] and not '/' in Args[3]:
                                    Symbolic_Link(os.path.join(os.getcwd(), Args[2]), os.path.join(os.getcwd(), Args[3]), send)
                                else:
                                    Symbolic_Link(Args[2], Args[3], send)
                            except:
                                pass
                        else:
                            try:
                                if not '/' in Args[1]:
                                    Symbolic_Link(os.path.join(os.getcwd(), Args[1]), Args[2], send)
                                else:
                                    Symbolic_Link(Args[1], Args[2], send)
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
                            send.superview['PrintTerminal'].text = Err
                except:
                    pass
            elif Args[0] == 'open':
                try:
                    console.quicklook(Args[1])
                except Exception as E:
                    send.superview['PrintTerminal'].text = E
            elif Args[0] == 'ping':
                try:
                    if not Args[1] == '-h':
                        if Args[1] == '-c':
                            try:
                                for _G in range(int(Args[2])):
                                    send.superview['PrintTerminal'].text = ping(Args[3])
                                    time.sleep(1)
                            except IndexError:
                                pass
                        else:
                            if Args[1] == '':
                                pass
                            else:
                                ping_list = []
                                for _ in range(3):
                                    ping_list.append(ping(Args[1]))
                                    time.sleep(1)
                                send.superview['PrintTerminal'].text = '\n'.join(ping_list)
                except:
                    pass
            elif Args[0] == 'pwd':
                try:
                    try:
                        PWD = os.getcwd()
                    except Exception as PWDErr:
                        PWD = PWDErr
                    send.superview['PrintTerminal'].text = PWD
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
                        send.superview['PrintTerminal'].text = Err
                except:
                    pass
            elif Args[0] == 'tar':
                TarArgument(Args, send)
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
                            except SystemExit:
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
                                wget(Args[1], send, filename=Args[3])
                            elif Args[2] == '--output':
                                wget(Args[1], send, filename=Args[3])
                        except IndexError:
                            wget(Args[1], send)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass
            elif Args[0] == 'zip':
                try:
                    if not Args[1] == '-h':
                        ZipArchiveCreate(Args[1], Args[2], send)
                except IndexError:
                    pass
                except:
                    pass
            elif Args[0] == 'exit':
                send.superview['PrintTerminal'].text = 'Exiting.......'
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
                run_other_cmd(Args[0], Args[1:], send)
        except KeyboardInterrupt:
            sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)

def clear():
    console.clear()

def chdirs(Location, send):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
    try:
        os.chdir(Location)
    except Exception as E:
        send.superview['PrintTerminal'].text = 'ERROR:{}'.format(E)

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

def git_clone(gitArgs, send):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
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
        send.superview['PrintTerminal'].text = 'Done'

def listdir(arg, pwd, send):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
    hOME = os.getenv('HOME')
    ListFiles = []
    if arg == 'long':
        listdirs = sorted(os.listdir())
        len_dir_lists = len(listdirs)
        for lis in range(len_dir_lists):
            if os.path.islink(os.path.join(pwd, listdirs[lis])):
                ListFiles.append('[%s] %s -> %s' % (time.strftime("%Y-%m-%d", time.localtime(os.stat(os.path.join(pwd, listdirs[lis])).st_mtime)),listdirs[lis], os.path.realpath(os.path.join(pwd, listdirs[lis])).replace(hOME, '~')))
            else:
                ListFiles.append('[%s] %s' % (time.strftime("%Y-%m-%d", time.localtime(os.stat(os.path.join(pwd, listdirs[lis])).st_mtime)),listdirs[lis]))
    elif arg == None:
        try:
            listdirs = sorted(os.listdir())
            len_dir_list = len(listdirs)
            for li in range(len_dir_list):
                ListFiles.append(listdirs[li])
        except Exception as E:
            send.superview['PrintTerminal'].text = E
    send.superview['PrintTerminal'].text = '\n'.join(ListFiles)

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

def run_stash_bin(cmdName, Sargs, send):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
    try:
        stash_bin_path = os.path.join(os.getenv('HOME'), 'Documents', 'stash_extensions', 'bin')
        Rcommand_name = cmdName + '.py'
        RfileName = os.path.join(stash_bin_path, Rcommand_name)
        RFile_read = open(RfileName, 'r', encoding='utf-8').read()
        sys.argv[1:] = Sargs
        try:
            exec(RFile_read)
        except SystemExit:
            pass
    except FileNotFoundError:
        pass
    except Exception as E:
        send.superview['PrintTerminal'].text = 'ERROR: {}'.format(E)

def run_other_cmd(cmd_name, args, send):
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
        run_stash_bin(cmd_name, args, send)
    except Exception as E:
        send.superview['PrintTerminal'].text = 'ERROR: {ERR}'.format(ERR=E)

def Symbolic_Link(Src, Dest, send):
    try:
        if os.path.isfile(Dest):
            send.superview['PrintTerminal'].text = '{DEs} Already Exists'.format(DEs=Dest)
            pass
        if os.path.islink(Dest):
            send.superview['PrintTerminal'].text = '{DEst} Already Linked'.format(DEs=Dest)
            pass
    except:
        pass
    try:
        os.symlink(Src, Dest)
    except Exception as E:
        send.superview['PrintTerminal'].text = 'Error: {ERR}.'.format(ERR=E)

def wget(URL, send, filename=''):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
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
        send.superview['PrintTerminal'].text = "Save as: {File} ".format(File=output_fileName)
        send.superview['PrintTerminal'].text = "({Size} bytes)".format(Size=fs if fs else "???")
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
            send.superview['PrintTerminal'].text = 'downloading.....'
            uu = requests.get(URL, headers=user_agent)
            try:
                File_size = int(uu.headers['Content-Length'])
            except  (IndexError, ValueError, TypeError):
                File_size = 0
            if uu.headers['Content-Type'] == 'application/json':
                with open(output_fileName, 'w') as F:
                    F.write(uu.json())
                send.superview['PrintTerminal'].text = 'save as {}'.format(output_fileName)
                send.superview['PrintTerminal'].text = "({} bytes)".format(File_size if File_size else "???")
            else:
                with open(output_fileName, 'wb') as Fb:
                    Fb.write(uu.content)
                send.superview['PrintTerminal'].text = 'Save as: {}'.format(output_fileName)
                send.superview['PrintTerminal'].text = "({} bytes)".format(File_size if File_size else "???")
        except Exception:
            send.superview['PrintTerminal'].text = 'Error. URL: {}'.format(URL)

def help_tar(send):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
    send.superview['PrintTerminal'].text = 'tar [-h] [-j] [-z] [-x] [file [files ...]]'
    send.superview['PrintTerminal'].text = 'Support Archive Type: tar.gz or tar.'
    send.superview['PrintTerminal'].text = 'This command is extract only.'

def TarArgument(ARGS, send):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
    try:
        if 'x' in ARGS[1][1:]:
            if 'z' in ARGS[1][1:]:
                try:
                    tExtract_ALL(os.path.join(os.getcwd(), ARGS[2][0:]), send, ARGS[1][1:])
                except:
                    pass
            elif 'j' in ARGS[1][1:]:
                try:
                    tExtract_ALL(os.path.join(os.getcwd(), ARGS[2][0:]), send, ARGS[1][1:])
                except:
                    pass
        elif ARGS[1][1:] == '--help':
            help_tar(send)
        elif 'h' in ARGS[1][1:]:
            help_tar(send)
        else:
            help_tar(send)
    except IndexError:
        help_tar(send)
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        pass

def ExtractMems(mem, ext):
    for tf in mem:
        for pt in ext:
            if tf.name == pt or tf.name.startswith(pt):
                yield tf

def tExtract_ALL(FName, tArgs, send, mems=None, Dir='./'):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
    if 'z' in tArgs[0]:
        send.superview['PrintTerminal'].text = 'Reading gzip file'
        tar = tarfile.open(FName, 'r:gz')
    elif 'j' in tArgs[0]:
        send.superview['PrintTerminal'].text = 'Reading bz2 file'
        tar = tarfile.open(FName, 'r:bz2')
    if mems:
        tar.extractall(path=Dir, members=ExtractMems(tar, mems))
    else:
        tar.extractall(path=Dir)
    tar.close()
    send.superview['PrintTerminal'].text = 'Archive Extracted'

def ZIPExtractor(zFileName, send):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
    if not os.path.isfile(zFileName):
        send.superview['PrintTerminal'].text = '{}: No such File...'.format(zFileName)
    else:
        try:
            pk_Check = open(zFileName, 'rb').read(2)
        except:
            pk_Check = ''
        if pk_Check != b'PK':
            send.superview['PrintTerminal'].text = '{}: Dose not appear to be a ZIPFile.'.format(zFileName)
        if os.path.basename(zFileName).lower().endswith('.zip'):
            ALPath = os.path.splitext(os.path.basename(zFileName))[0]
        else:
            ALPath = os.path.basename(zFileName) + '_UnZIPPED'
        ALPath = os.path.join(os.path.dirname(zFileName), ALPath)
        if (os.path.exists(ALPath)) and not (os.path.isdir(ALPath)):
            send.superview['PrintTerminal'].text = '{}: Destination is not a Directory.'.format(ALPath)
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
                send.superview['PrintTerminal'].text = Fn
        except:
            send.superview['PrintTerminal'].text = '{}: ZIP File is Corrupt'.format(zFileName)

def ZipArchiveCreate(ziPFilename, IPath, send):
    send.superview['PrintTerminal'].text = send.superview['PrintTerminal'].text
    REL_ROOT = os.path.abspath(os.path.dirname(ziPFilename))
    with zipfile.ZipFile(ziPFilename, 'w', zipfile.ZIP_DEFLATED) as OutPutsZip:
        if os.path.isfile(IPath):
            send.superview['PrintTerminal'].text = IPath
            ARCHiveName = os.path.relpath(IPath, REL_ROOT)
            OutPutsZip.write(IPath, arcname=ARCHiveName)
        elif os.path.isdir(IPath):
            for Root, Dir, Files in os.walk(IPath):
                TH_RELROOT = os.path.relpath(Root, REL_ROOT)
                OutPutsZip.write(Root, arcname=TH_RELROOT)
                send.superview['PrintTerminal'].text = TH_RELROOT
                for _Fi in Files:
                    Fi_Name = os.path.join(Root, _Fi)
                    if os.path.isfile(Fi_Name):
                        send.superview['PrintTerminal'].text = Fi_Name
                        ARCHIVE_NAME = os.path.join(TH_RELROOT, _Fi)
                        OutPutsZip.write(Fi_Name, arcname=ARCHIVE_NAME)

def main(send):
    _input = send.superview['TerminalCmd'].text
    __init__()
    try:
        try:
            INPUT_Argument = _input.split(' ')
            Argument_Paser(INPUT_Argument, send)
        except KeyboardInterrupt:
            sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(0)
    send.superview['TerminalCmd'].text = ''

v = ui.load_view_str(SheetStr())
v['Logo'].text = SystemLogo()
v.present('panel')
