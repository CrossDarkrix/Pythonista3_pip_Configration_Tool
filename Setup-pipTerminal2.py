import sys
from pathlib import Path
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

v_maj, v_min, v_patch, *_ = sys.version_info
assert v_maj >= 3, "Python 3.10 or a more recent version is required."
assert v_min >= 10, "Python 3.10 or a more recent version is required."

pipTerminal_URL = f"https://raw.githubusercontent.com/o-murphy/Pythonista3_pip_Configration_Tool/main/pipTerminal.py"
getPipBootstrap_URL = "https://bootstrap.pypa.io/get-pip.py"


HOME = Path("~").expanduser()
DOCUMENTS = HOME / "Documents"
pipTerminal_DST = DOCUMENTS / "pipTerminal.py"


def installation_pipTerminal():
    with open(pipTerminal_DST, "w") as terminal:
        terminal.write(requests.get(pipTerminal_URL).content.decode(errors="ignore"))


def installation_realpip():
    code = requests.get(getPipBootstrap_URL).content.decode(errors="ignore")
    # This is the dangerous part
    try:
        exec(code, {"__name__": "__main__"})
    except KeyboardInterrupt:
        pass


def main():
    print("Save pipTerminal.........")
    installation_pipTerminal()
    print(f"Successful Save pipTerminal! save path: {pipTerminal_DST}")
    print("Install Real pip.........")
    installation_realpip()
    print("All Installation Done!")
    print("Please Restart Pythonista!")


if __name__ == "__main__":
    main()
