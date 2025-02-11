import json
from control.__control_settings__ import CONTROL_SETTINGS_PATH, LANGUAGE_DIALOG_PATH

class Settings:
    def load_language(self, language):
        with open(LANGUAGE_DIALOG_PATH + "en-en.json", "r") as file:
            default_dialogs = json.load(file)
        with open(LANGUAGE_DIALOG_PATH + language + ".json", "r") as file:
            dialogs = json.load(file)
        default_dialogs.update(dialogs)
        return default_dialogs

    def load_settings(self):
        """
            load settings from json file with set path
        """
        with open(CONTROL_SETTINGS_PATH, "r") as file:
            settings = json.load(file)
        return settings
    
    def save_settings(self, settings):
        """
            save settings into json file with set path
        """
        with open(CONTROL_SETTINGS_PATH, "w") as file:
            json.dump(settings, file, indent=4)