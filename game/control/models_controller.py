import pygame as pg
import abc

from game.control.control import Control

class Models_controller(Control, abc.ABC):
    """
    Base controller class for handling game models. 
    This class serves as an abstract controller for managing different game states and interactions.
    """
    player_pokedex = None
    new_battle = None

    def __init__(self):
        self.done = False
        self.quit = False
        self.next = None
        self.previous = None

    @classmethod
    def init_in_game_settings(cls):
        """
            retrive settings and dialogs dict from Control to update all
            depending variables upon start of program like fonts and sizes, 
            sound channels and volumes as well as shared assets
        """
        cls.__init_game_settings__()

        ### PATHS ASSIGNMENT ###
        cls.POKEMON_CLASSIC_PATH = cls.FONTS_PATH + cls.POKEMON_CLASSIC_FONT

        ### VIEWS VARIABLES INIT ###
        cls.__init_display_settings__()
        cls.__init_sounds_settings__()

        ## VIEWS ASSETS LOAD ###
        cls.__load_sounds_menues__()
    
    @classmethod
    def re_init_in_game_settings(cls):
        """
            redefine variables that depend on current settings while
            avoiding reloading any assets
        """
        cls.__init_game_settings__()

        ### VIEWS VARIABLES INIT ###
        cls.__init_display_settings__()
        cls.__init_sounds_settings__()

        ## UPDATE EACH MENU PROPORTIONS ###
        for menu in Control.STATE_DICT.values():
            menu.update_in_game_settings()
    
    @classmethod
    def __init_game_settings__(cls):
        cls.settings = Control.settings
        cls.dialogs = Control.dialogs
        for setting in cls.settings.keys():
            setattr(cls, setting, cls.settings[setting])
        cls.screen_rect = cls.screen.get_rect()
    
    @classmethod
    def __init_display_settings__(cls):
        cls.width = cls.screen_rect.width
        cls.height = cls.screen_rect.height

        cls.pixel_font_pokemon_infos = pg.font.Font(
            cls.POKEMON_CLASSIC_PATH, int(cls.width*0.022)
        )
        cls.pixel_font_menu_deselected = pg.font.Font(
            cls.POKEMON_CLASSIC_PATH, int(cls.width*0.022)
        )
        cls.pixel_font_menu_selected = pg.font.Font(
            cls.POKEMON_CLASSIC_PATH, int(cls.width*0.027)
        )
    
    @classmethod
    def __init_sounds_settings__(cls):
        cls.music_channel = pg.mixer.Channel(0)
        cls.music_channel.set_volume(
            cls.music_volume*0.08
        )
        cls.effects_channel = pg.mixer.Channel(1)
        cls.effects_channel.set_volume(
            cls.sfx_volume*0.4
        )
        cls.double_effects_channel = pg.mixer.Channel(2)
        cls.double_effects_channel.set_volume(
            cls.sfx_volume*0.2
        )
        cls.menu_effects_channel = pg.mixer.Channel(2)
        cls.menu_effects_channel.set_volume(
            cls.sfx_volume*0.3
        )

    @classmethod
    def __load_sounds_menues__(cls):
        cls.menues_sounds = {
            "cursor move" : pg.mixer.Sound(cls.SFX_PATH+"cursor move.wav"),
            "confirm" : pg.mixer.Sound(cls.SFX_PATH+"confirm sound.wav"),
            "back" : pg.mixer.Sound(cls.SFX_PATH+"hit_no_effective.mp3"),
            "save success" : pg.mixer.Sound(cls.SFX_PATH+"save_success.mp3"),
            "quit game" : pg.mixer.Sound(cls.SFX_PATH+"run-away.mp3")
        }

    def blit_dialog(self, dialog : str, size : int,
            from_left, from_top, placement_origin : str = "midbottom",
            color : tuple=(0,0,0), bold : bool=False):
        """
            Renders and displays a dialog on the screen. The text can be customized with different sizes,
            positions, colors, and boldness.
        """
        font = pg.font.Font(self.POKEMON_CLASSIC_PATH, int(size))
        font.set_bold(bold)
        text = font.render(dialog, True, color)
        if placement_origin == "midbottom":
            text_rect = text.get_rect(midbottom=(from_left,from_top))
        elif placement_origin == "bottomleft":
            text_rect = text.get_rect(bottomleft=(from_left,from_top))
        self.screen.blit(text, text_rect)

    # @abc.abstractmethod
    # def startup(self):
    #     pass

    # @abc.abstractmethod
    # def update(self):
    #     pass

    # @abc.abstractmethod
    # def cleanup(self):
    #     pass