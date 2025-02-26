import pygame as pg

from game.models.menu_models.option_menu_model import Option_menu_model

class Main_menues_display:
    """
        Class for managing the main menus display. It includes
        the title menu, preferences menu, and load menu.
    """
    def init_main_menu_display(self):
        self.init_root_variables_main_menu()
        self.load_backgrounds_main_menues()
    
    def init_root_variables_main_menu(self):
        """
            Sets up initial variables for title menu, preferences menu, and load menu
        """
        self.title_menu_variables : tuple = (
            self.width*0.3, self.height*0.42, self.height*0.1
        )
        self.preferences_menu_variables : tuple = (
            self.width*0.5, self.height*0.146, self.height*0.1243
        )
        self.load_menu_variables : tuple = (
            self.width*0.5, self.height/3, self.height*0.1
        )

    ### TITLE MENU ###
    def init_title_menu_object(self):
        self.title_menu = Option_menu_model(
            self.title_menu_variables,
            self.init_render_option_title_menu(),
            ["load_menu", "preferences_menu", "quit"],
            (0,0,0), (255,255,0)
        )
    
    def update_title_menu_objects(self):
        self.title_menu.update_options(
            self.init_render_option_title_menu(),
            margins=self.title_menu_variables
        )
    
    def init_render_option_title_menu(self):
        options = [
            self.dialogs['play'],
            self.dialogs['options'], 
            self.dialogs['quit']
        ]
        return options
    
    ### PREFERENCES MENU ###
    def init_preferences_menu_objects(self):
        self.preferences_menu = Option_menu_model(
            self.preferences_menu_variables,
            self.init_render_option_preferences_menu(),
            ["", "", "", "", "", "title_menu"],
            (255,255,255),(32,215,192)
        )

    def update_preferences_menu_objects(self):
        self.preferences_menu.update_options(
            self.init_render_option_preferences_menu(),
            margins=self.preferences_menu_variables
        )
    
    def init_render_option_preferences_menu(self):
        """
            Generates the options for the preferences menu based on the current settings
        """
        if self.settings_in_preferences == []:
            return []
        options = [
            self.dialogs['sfx volume'] + str(self.settings_in_preferences['sfx_volume']),
            self.dialogs['music volume'] + str(self.settings_in_preferences['music_volume']),
            self.dialogs['language'] + self.LANGUAGES_DICT[self.settings_in_preferences['language']],
            self.dialogs['screen resolution'] + self.SCREEN_RESOLUTION_DICT[self.settings_in_preferences['screen_resolution']],
            self.dialogs['apply'], 
            self.dialogs['back']
        ]
        return options

    ### LOAD MENU ###
    def init_load_menu_objects(self):
        self.load_menu = Option_menu_model(
            self.load_menu_variables,
            *self.init_render_option_load_menu(),
            (0,0,0),(80,96,176)
        )

    def update_load_menu_objects(self):
        self.load_menu.update_options(
            *self.init_render_option_load_menu(),
            margins=self.load_menu_variables
        )

    def init_render_option_load_menu(self):
        """
            Generates the options for the load menu based on available saved games
        """
        options = [self.dialogs['new game']]
        next_list = ["new_game"]
        for player_save in self.player_saves_state:
            if player_save == {}:
                options.append("")
                next_list.append("")
            else:
                options.append(player_save['player'])
                next_list.append("launch_menu")
        options.append(self.dialogs['back'])
        next_list.append("title_menu")
        return options, next_list

    ### GRAPHICS LOAD AND RENDER ###
    def load_backgrounds_main_menues(self):
        """
            Loads and scales the graphics for the title, preferences, and load menus.
        """
        self.main_menues_backgrounds_assets_dict : dict = {
            "title_background" : pg.image.load(
                self.GRAPHICS_PATH+"/media/"+"title screen.png"
            ),
            "preferences_background" : pg.image.load(
                self.GRAPHICS_PATH+"/media/"+"preferences screen.png"
            ),
            "load_background" : pg.image.load(
                self.GRAPHICS_PATH+"/media/"+"load screen.png"
            )
        }
        self.pre_render_backgrounds_main_menues()
    
    def pre_render_backgrounds_main_menues(self):
        self.main_menues_backgrounds_scaled_dict : dict = {
            "title_background" : pg.transform.scale(
                self.main_menues_backgrounds_assets_dict[
                    "title_background"],
                (self.width, self.height)
            ),
            "preferences_background" : pg.transform.scale(
                self.main_menues_backgrounds_assets_dict[
                    "preferences_background"],
                (self.width, self.height)
            ),
            "load_background" : pg.transform.scale(
                self.main_menues_backgrounds_assets_dict[
                    "load_background"],
                (self.width, self.height)
            )
        }

    def draw_title_screen(self):
        self.screen.blit(
            self.main_menues_backgrounds_scaled_dict[
                "title_background"], 
            (0,0)
        )

    def draw_load_screen(self):
        self.screen.blit(
            self.main_menues_backgrounds_scaled_dict[
                "load_background"],
            (0,0)
        )
    
    def draw_preferences_screen(self):
        self.screen.blit(
            self.main_menues_backgrounds_scaled_dict[
                "preferences_background"],
            (0,0)
        )
