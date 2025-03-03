import pygame as pg

from game.control.control import Control
from game.control.models_controller import Models_controller
from game.models.pokemons.pokedex import Pokedex

from game.models.main_menu_models.title_menu import Title_menu
from game.models.main_menu_models.preferences_menu import Preferences_menu
from game.models.main_menu_models.load_menu import Load_menu
from game.models.in_game_models.new_game import New_game
from game.models.in_game_models.launch_menu import Launch_menu
from game.models.in_game_models.in_battle import In_battle

pg.init()

game = Control()
game.init_settings()
game.init_config()
Models_controller.init_in_game_settings()
Pokedex.init_pokedex_data([
            Models_controller.POKEMON_DICT_PATH,
            Models_controller.TYPES_CHART_PATH,
            Models_controller.BATTLE_BIOMES_PATH
        ])

STATE_DICT = {
    "title_menu" : Title_menu(),
    "preferences_menu" : Preferences_menu(),
    "new_game" : New_game(),
    "load_menu" : Load_menu(),
    "in_battle" : In_battle(),
    "launch_menu" : Launch_menu()
}

game.setup_states(STATE_DICT, "title_menu")

game.main_game_loop()

pg.quit()