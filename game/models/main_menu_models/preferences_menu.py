import pygame as pg

from game.control.models_controller import Models_controller
from game.views.main_menu_views.main_menues_display import Main_menues_display
from game.views.main_menu_views.main_menues_sounds import Main_menues_sounds

class Preferences_menu(
    Models_controller, 
    Main_menues_display, Main_menues_sounds):
    """
        A class representing the preferences menu, allowing the user to adjust various settings
        such as volume, language, and screen resolution.
    """
    def __init__(self):
        Models_controller.__init__(self)
        self.init_main_menu_display()
        self.init_main_menues_sounds()
        self.settings_in_preferences = []
        self.init_preferences_menu_objects()

    def update_in_game_settings(self):
        self.init_root_variables_main_menu()
        self.pre_render_backgrounds_main_menues()

    def startup(self):
        """
            Initializes all menu-related data, loads settings, and prepares the menu display.
        """
        self.settings_in_preferences = self.settings.copy()
        self.update_preferences_menu_objects()

    def update(self):
        """
            update the menu with all new informations such as hovering or
            selecting an option as well as playing a sound when happening,
            then launch draw method
        """
        self.draw()

    def cleanup(self):
        """
            cleans up all menu related data
        """
        pass

    def get_event(self, event):
        """
           Handles user inputs and responds to key events for menu navigation and settings adjustments
        """
        if event.type == pg.QUIT:
            self.quit = True
        if event.type == pg.KEYDOWN:
            if pg.key.name(event.key) in self.return_keys and not self.quit:
                self.menu_effects_channel.play(self.menues_sounds["back"])
                self.next = "title_menu"
                self.done = True
            if pg.key.name(event.key) in self.confirm_keys and\
                    self.preferences_menu.selected_index == len(
                    self.preferences_menu.next_list) - 1:
                self.menu_effects_channel.play(self.menues_sounds["confirm"])
                self.select_option(self.preferences_menu)
            elif pg.key.name(event.key) in self.confirm_keys\
                and self.preferences_menu.selected_index == 4 and\
                    self.settings_in_preferences != self.settings:
                self.menu_effects_channel.play(self.menues_sounds["confirm"])
                self.save_settings(self.settings_in_preferences)
                self.init_settings()
                self.init_config()
                Models_controller.re_init_in_game_settings()
                self.startup()
                self.effects_channel.play(self.menues_sounds["save success"])
            elif pg.key.name(event.key) in self.left_keys:
                self.menu_effects_channel.play(self.menues_sounds["confirm"])
                self.change_settings(-1)
            elif pg.key.name(event.key) in self.right_keys:
                self.menu_effects_channel.play(self.menues_sounds["confirm"])
                self.change_settings(1)

        self.preferences_menu.get_event_vertical(event)

    def select_option(self, menu):
        """
            change the active state with done attribute and change it
            to correct user input
        """
        self.next = menu.next_list[menu.selected_index]
        self.done = True

    def change_settings(self, operant):
        """
        Modifies the selected setting value based on user input.
        """
        OPTIONS = (("", self.settings_in_preferences['sfx_volume'], 'sfx_volume'),
                ("", self.settings_in_preferences['music_volume'], 'music_volume'),
                (self.LANGUAGES_DICT, self.settings_in_preferences['language'], 'language'),
                (self.SCREEN_RESOLUTION_DICT, self.settings_in_preferences['screen_resolution'], 'screen_resolution'))
        index = self.preferences_menu.selected_index

        if index in (0,1):
            current_setting_index = OPTIONS[index][1]
            selected_setting_index = current_setting_index + operant

            if selected_setting_index < 0:
                selected_setting_index = 0
            elif selected_setting_index > 10:
                selected_setting_index = 10

            self.settings_in_preferences[OPTIONS[index][2]] = selected_setting_index
            
        elif index in (2,3):
            options_list = list(OPTIONS[index][0].keys())
            current_setting_index = options_list.index(OPTIONS[index][1])
            selected_setting_index = current_setting_index + operant
            if selected_setting_index < 0:
                selected_setting_index = len(options_list) - 1
            elif selected_setting_index > len(options_list) - 1:
                selected_setting_index = 0
            
            self.settings_in_preferences[OPTIONS[index][2]] = options_list[selected_setting_index]

        if index == 0:
            self.settings_in_preferences['sfx_volume'] = selected_setting_index
        elif index == 1:
            self.settings_in_preferences['music_volume'] = selected_setting_index
        elif index == 2:
            self.settings_in_preferences['language'] = options_list[selected_setting_index]
        elif index == 3:
            self.settings_in_preferences['screen_resolution'] = options_list[selected_setting_index]
        
        self.update_preferences_menu_objects()
    
    def draw(self):
        """
            launch all display related scripts proper to this menu back
            the main_menu states shared scripts
        """
        self.draw_preferences_screen()
        self.preferences_menu.draw_vertical_options()