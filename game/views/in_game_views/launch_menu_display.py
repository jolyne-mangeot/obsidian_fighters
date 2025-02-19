import pygame as pg

from game.views.in_game_views.game_menues_display import Game_menues_display
from game.models.menu_models.option_menu_model import Option_menu_model

class Launch_menu_display(Game_menues_display):
    def init_launch_menu_display(self):
        self.init_in_game_display()
        self.init_root_variables_launch_menu()
        self.init_menues_objects()

    def init_root_variables_launch_menu(self):

        self.confirm_menu_variables : tuple = (
            self.width*0.5, self.height*0.5, self.height*0.09
        )
        self.main_menu_variables : tuple = (
            self.width*0.5, self.height*0.36, self.height*0.09
        )
        self.save_menu_variables : tuple = (
            self.width*0.5, self.height*0.44, self.height*0.09
        )
        self.pokedex_menu_variables : tuple = (
            self.width*0.75, self.height*0.45, self.height*0.15,
        )
        self.pokedex_menu_colors : tuple = (
            None, (255,255,255), (43,250,250)
        )
    
    def init_render_option_pokedex(self):
        options = []
        for pokemon in list(self.player_pokedex.pokemon_dict.keys()):
            entry = "#" + self.player_pokedex.pokemon_dict[pokemon]["entry"]
            name = self.dialogs[self.player_pokedex.pokemon_dict[pokemon]["name"]]
            option = entry
            while len(option) < 16:
                option += " "
            option += name
            options.append(option)
        return options

    
    def load_pokedex_mini_images(self):
        mini_images = []
        for pokemon in list(self.player_pokedex.pokemon_dict.keys()):
            mini_image = pg.image.load(
                self.GRAPHICS_PATH +"pokemon/"+\
                self.player_pokedex.pokemon_dict[pokemon]["entry"]+"/mini.png")
            mini_image = pg.transform.scale(
                mini_image,(self.width*0.2,self.width*0.17)
            )
            mini_images.append(mini_image)
        return mini_images
    
    def init_menues_objects(self):
        self.main_launch_menu = Option_menu_model(
            self.main_menu_variables,
            [
                self.dialogs["launch"],
                self.dialogs["pokedex"],
                self.dialogs["manage team"],
                self.dialogs["save"],
                self.dialogs["quit"]
            ],
            ["launch_battle_confirm", "pokedex_menu", "manage_team", "save", "quit"]
        )
        self.manage_team_menu = Option_menu_model(
            self.main_menu_variables,
            self.init_render_option_team(self.player_pokedex.player_team)
        )
        self.display_pokedex_menu = Option_menu_model(
            self.pokedex_menu_variables,
            self.init_render_option_pokedex(),
            *self.pokedex_menu_colors,
            images=self.load_pokedex_mini_images()
        )
        self.confirm_action_menu = Option_menu_model(
            self.confirm_menu_variables,
            [self.dialogs["no"], self.dialogs["yes"]],
        )
        self.save_menu = Option_menu_model(
            self.save_menu_variables,
            [
                self.dialogs["save_1"],
                self.dialogs["save_2"],
                self.dialogs["back"]
            ]
        )
        self.main_launch_menu.update_colors((0,0,0),(80,96,176))
        self.confirm_action_menu.update_colors((0,0,0),(80,96,176))
        self.manage_team_menu.update_colors((0,0,0),(80,96,176),(255,0,0))

    def draw(self):
        """
            init all display related script
        """
        self.draw_launch_menu()
        self.options_menu_draw_dict[self.menu_state]()

    def draw_main_launch_menu(self):
        self.main_launch_menu.draw_vertical_options()

    def draw_launch_battle_confirm_menu(self):
        self.confirm_action_menu.draw_vertical_options()
    
    def draw_pokedex_menu(self):
        self.draw_pokedex_background()
        self.display_pokedex_menu.draw_list_options()
        self.draw_focused_pokemon()
    
    def draw_focused_pokemon(self):
        if self.focused_pokemon != None:
            self.screen.blit(
                self.display_pokedex_menu.images[int(self.focused_pokemon)-1],
                (self.width*0.18, self.height*0.16)
            )
            self.blit_dialog(
                "#" +\
                    self.player_pokedex.pokemon_dict[self.focused_pokemon]["entry"],
                self.width*0.027, self.width*0.1, self.height*0.23,
                "bottomleft", bold=True,
            )
            self.blit_dialog(
                self.dialogs[self.player_pokedex.pokemon_dict[self.focused_pokemon]["name"]],
                self.width*0.022, self.width*0.06, self.height*0.31,
                "bottomleft", bold=True,
            )
            self.blit_dialog(
                self.dialogs["stat attack"] +\
                    str(self.player_pokedex.pokemon_dict[self.focused_pokemon]["base_attack"]),
                self.width*0.022, self.width*0.06, self.height*0.36,
                "bottomleft", bold=True,
            )
            self.blit_dialog(
                self.dialogs["stat defense"] +\
                    str(self.player_pokedex.pokemon_dict[self.focused_pokemon]["base_defence"]),
                self.width*0.022, self.width*0.06, self.height*0.4,
                "bottomleft", bold=True,
            )
            self.blit_dialog(
                self.dialogs["stat health points"] +\
                    str(self.player_pokedex.pokemon_dict[self.focused_pokemon]["base_health_points"]),
                self.width*0.022, self.width*0.06, self.height*0.45,
                "bottomleft", bold=True,
            )

    def draw_manage_team_menu(self):
        self.manage_team_menu.draw_picked_options()
    
    def draw_save_menu(self):
        self.save_menu.draw_vertical_options()
        self.blit_dialog(
            self.dialogs["save menu"],
            self.width*0.025,
            self.width*0.5, self.height*0.29
        )
    
    def draw_save_confirm_menu(self):
        self.confirm_action_menu.draw_vertical_options()

    def draw_delete_save_confirm_menu(self):
        self.confirm_action_menu.draw_vertical_options()

    def draw_launch_menu_lost_game(self):
        self.blit_dialog(
            self.dialogs["lost save"],
            self.width*0.032,
            self.width*0.5, self.height*0.5,
            bold = True
        )
        self.blit_dialog(
            self.dialogs["delete save tip"],
            self.width*0.022,
            self.width*0.5, self.height*0.62,
            bold = True
        )
    
    def draw_quit_confirm_menu(self):
        self.confirm_action_menu.draw_vertical_options()