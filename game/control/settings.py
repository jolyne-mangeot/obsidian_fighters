import json
import os

class Settings:
    """
        Handles all parameters from imported settings.json file
    """

    def load_player_data(self) -> dict:
        """
            Loads all player save data from the saves directory
        """
        player_saves = []
        for save_path in self.SAVES_PATH:
            with open(save_path, "r") as file:
                player_saves.append(json.load(file))
        return player_saves

    def load_language(self, language_path : str, language : str) -> dict:
        """
            Load the default English dialogues
        """
        with open(language_path + "en-en.json", "r") as file:
            default_dialogs = json.load(file)
        with open(language_path + language + ".json", "r") as file:
            dialogs = json.load(file)
        default_dialogs.update(dialogs)
        return default_dialogs
    
    def save_player_data(self, player_data : dict, save : str):
        """
            Saves player data into a JSON file
        """
        with open(self.SAVE_PATH + "save_" + save + "_pokedex.json", "w") as file:
            json.dump(player_data, file, indent=4)
    
    def reset_player_data(self, save : str):
        """
            Resets player save data by overwriting the file with an empty dictionary
        """
        with open(self.SAVE_PATH + "save_" + save + "_pokedex.json", "w") as file:
            json.dump({}, file, indent=4)     

    def load_settings(self):
        """
            load settings from json file with set path
        """
        with open(self.find_settings_file(), "r") as file:
            settings = json.load(file)
        return settings
    
    def save_settings(self, settings):
        """
            save settings into json file with set path
        """
        with open(self.find_settings_file(), "w") as file:
            json.dump(settings, file, indent=4)
    
    def find_settings_file(self):
        for root, dirs, files in os.walk("game/"):
            if "settings.json" in files:
                return os.path.join(root, "settings.json")