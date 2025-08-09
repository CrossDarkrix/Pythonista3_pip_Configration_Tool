import sys
from pathlib import Path
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

v_maj, v_min, v_patch, *_ = sys.version_info
assert v_maj >= 3, "Python 3.10 or a more recent version is required."
assert v_min >= 10, "Python 3.10 or a more recent version is required."

pipTerminal_URL = f"https://raw.githubusercontent.com/CrossDarkrix/Pythonista3_pip_Configration_Tool/main/pipTerminal.py"
getPipBootstrap_URL = "https://bootstrap.pypa.io/get-pip.py"


HOME = Path("~").expanduser()
DOCUMENTS = HOME / "Documents"
pipTerminal_DST = DOCUMENTS / "pipTerminal.py"


def pin_shortcut():
    """Creates or updates a shortcut for the 'pipTerminal' script in Pythonista's action menu."""
    try:
        from objc_util import ObjCClass, ns

        NSUserDefaults = ObjCClass("NSUserDefaults")

        def get_actions():
            defaults = NSUserDefaults.standardUserDefaults()
            return list(defaults.arrayForKey_("EditorActionInfos") or ())

        def save_defaults():
            defaults = NSUserDefaults.standardUserDefaults()
            NSUserDefaults.setStandardUserDefaults_(defaults)

        def remove_action_at_index(index):
            defaults = NSUserDefaults.standardUserDefaults()
            editoractions = get_actions()
            del editoractions[index]
            defaults.setObject_forKey_(editoractions, "EditorActionInfos")

        def add_action(scriptName, iconName, iconColor, title):
            defaults = NSUserDefaults.standardUserDefaults()
            kwargs = locals()
            entry = {
                key: kwargs[key]
                for key in ("scriptName", "iconName", "iconColor", "title", "arguments")
                if key in kwargs and kwargs[key]
            }
            editoractions = get_actions()
            editoractions.append(ns(entry))
            defaults.setObject_forKey_(editoractions, "EditorActionInfos")

        pipTerminal_action = {
            "scriptName": "pipTerminal.py",
            "title": "pipTerminal",
            "iconColor": "000000",
            "iconName": "Primaries_ChevronRight",
        }

        script_path = pipTerminal_action["scriptName"]
        full_script_path = Path("~").expanduser() / "Documents" / script_path

        if not full_script_path.exists():
            raise FileNotFoundError(
                f"Error: The 'pipTerminal' script was not found at {full_script_path}."
            )

        current_actions = get_actions()
        script_names = [str(action["scriptName"]) for action in current_actions]

        if script_path in script_names:
            index_to_remove = script_names.index(script_path)
            remove_action_at_index(index_to_remove)

        add_action(**pipTerminal_action)
        save_defaults()
        print("Success: New 'pipTerminal' shortcut created.")

    except Exception:
        print(f"Unable to create 'pipTerminal' shortcut.")


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
    print("Creating shortcut")
    pin_shortcut()
    print("All Installation Done!")
    print("Please Restart Pythonista!")


if __name__ == "__main__":
    main()
