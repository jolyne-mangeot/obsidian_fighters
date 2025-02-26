import pygame as pg

from game.views.in_game_views.game_menues_display import Game_menues_display
from game.models.menu_models.option_menu_model import Option_menu_model
from game.models.menu_models.input_menu_model import Input_menu_model

class New_game_display(Game_menues_display):
    """
        This class is responsible for displaying the New Game screen where the player can 
        select their starter Pokémon and input their name.
    """
    def init_new_game_display(self):
        self.__init_root_variables_new_game__()
        self.__load_assets_new_game__()
        self.__init_menues_objects__()
    
    def update_new_game_display(self):
        self.__init_root_variables_new_game__()
        self.__pre_render_assets_new_game__()
        self.__update_menues_objects__()

    def __init_root_variables_new_game__(self):
        """
        Initializes root variables specifically for the New Game screen, such as positions
        for player input and Pokémon choice.
        """

        self._init_root_variables_in_game_()
        
        self.player_input_variables : tuple = (
            self.width*0.5, self.height*0.5
        )
        self.pokemon_choice_variables : tuple = (
            self.width*0.5, self.height*0.6, 60
        )

    def __init_menues_objects__(self):
        """
        Initializes the menu objects for player name input and Pokémon selection.
        """
        self.player_input = Input_menu_model(
            self.player_input_variables,
            self.init_render_option_player_input()
        )
        self.pokemon_choice = Option_menu_model(
            self.pokemon_choice_variables,
            self.init_render_option_pokemon_choice(),
            (0,0,0), (43,255,255)
        )
    
    def init_render_option_player_input(self) -> str:
        dialog : str = self.dialogs["your name"]
        return dialog
    
    def init_render_option_pokemon_choice(self) -> list:
        options : list = [
            self.dialogs[pokemon["name"]] for pokemon\
            in self.pokemon_starters
        ]
        return options

    def __update_menues_objects__(self):
        self.player_input.update_options(
            self.player_input_variables,
            self.init_render_option_player_input()
        )
        self.pokemon_choice.update_options(
            self.init_render_option_pokemon_choice(),
            margins=self.pokemon_choice_variables
        )
    
    def __load_assets_new_game__(self):
        self.new_game_assets_dict : dict = {
            "starters_frame" : pg.image.load(
                self.GRAPHICS_PATH+"/media/"+\
                "pkmn frame.png"
            ),
            "starters_mini" : self.load_starters_mini(),
            "new_game_background" : pg.image.load(
                self.GRAPHICS_PATH+"/media/"+\
                "pkmn choice bg.png"
            ),
        }
        self.__pre_render_assets_new_game__()

    def load_starters_mini(self) -> list:
        pokemon_starters_image : list = []
        for pokemon in self.pokemon_starters:
            mini_image = pg.image.load(
                self.GRAPHICS_PATH + "pokemon/" +\
                pokemon["entry"] + "/mini.png"
            )
            pokemon_starters_image.append(mini_image)
        return pokemon_starters_image
    

    def __pre_render_assets_new_game__(self):
        self.new_game_assets_scaled_dict : dict = {
            "starters_frame" : pg.transform.scale(
                self.new_game_assets_dict["starters_frame"],
                (self.width*0.2, self.width*0.2)
            ),
            "starters_mini" : self.pre_render_starters_mini(),
            "player_frame" : pg.transform.scale(
                self.new_game_assets_dict["starters_frame"],
                (self.width*0.62, self.height*0.07)
            ),
            "new_game_background" : pg.transform.scale(
                self.new_game_assets_dict["new_game_background"],
                (self.width,self.height)
            )
        }

    def pre_render_starters_mini(self) -> list:
        """
        Loads mini-images of starter Pokémon, scales them to fit the display, 
        and stores them in a list for later drawing
        """
        pokemon_starters_image : list = []
        for image in self.new_game_assets_dict["starters_mini"]:
            mini_image = pg.transform.scale(
                image, (self.width*0.5, self.width*0.42)
            )
            pokemon_starters_image.append(mini_image)
        return pokemon_starters_image

    def draw(self):
        """
            init all display related script
        """
        self.draw_new_game_background()
        self.options_menu_draw_dict[self.menu_state](self.menu_state)

    def draw_new_game_background(self):
        self.screen.blit(
            self.new_game_assets_scaled_dict["new_game_background"],
            (0,0)
        )

    def draw_player_input_menu(self, none=None):
        self.draw_name_frame()
        self.player_input.draw_input()
    
    def draw_pokemon_choice_menu(self, none=None):
        self.pokemon_choice.draw_horizontal_options()
        self.draw_starter_pokemon()

    def draw_pokemon_frame(self, index):
        starter_frame_rect = self.new_game_assets_scaled_dict[
                "starters_frame"].get_rect(
            center=(self.width*0.25 * (index+1), self.height*0.43)
        )
        self.screen.blit(
            self.new_game_assets_scaled_dict["starters_frame"],
            starter_frame_rect
        )

    def draw_name_frame(self):
        player_name_frame_rect = self.new_game_assets_scaled_dict[
                "player_frame"].get_rect(
            center=(self.width*0.5, self.height*0.5)
        )
        self.screen.blit(
            self.new_game_assets_scaled_dict["player_frame"],
            player_name_frame_rect
        )

    def draw_starter_pokemon(self):
        for index, image in enumerate(
                self.new_game_assets_scaled_dict["starters_mini"]):
            self.draw_pokemon_frame(index)
            self.screen.blit(image, (self.width*0.25 * index, self.height*0))
