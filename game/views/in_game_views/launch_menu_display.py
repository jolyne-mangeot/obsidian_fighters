import pygame as pg

from game.models.menu_models.option_menu_model import Option_menu_model

class Launch_menu_display:
    """
        The Launch_menu_display class is responsible for displaying and managing the in-game launch menu.
        It inherits from Game_menues_display.
    """
    def init_launch_menu_display(self):
        self.__init_root_variables_launch_menu__()
        self.load_assets_launch_menu()
        self.__init_menues_objects__()
    
    def update_launch_menu_display(self):
        self.__init_root_variables_launch_menu__()
        self._pre_render_assets_launch_menu_()
        self.update_menues_objects()

    def __init_root_variables_launch_menu__(self):
        """
            Initializes the root variables for the launch menu, including positions and dimensions 
            for various menus such as confirm, main, and save menus.
        """
        self.confirm_menu_variables : tuple = (
            self.width*0.5, self.height*0.5, self.height*0.09
        )
        self.main_menu_variables : tuple = (
            self.width*0.5, self.height*0.36, self.height*0.09
        )
        self.launch_battle_menu_variables : tuple = (
            self.width*0.5, self.height*0.56, self.height*0.09
        )
        self.save_menu_variables : tuple = (
            self.width*0.5, self.height*0.44, self.height*0.09
        )
        self.pokedex_menu_variables : tuple = (
            self.width*0.75, self.height*0.45, self.height*0.15,
        )
        self.mini_image_size : tuple = (
            self.width*0.2, self.width*0.17
        )

    def __init_menues_objects__(self):
        """
            Initializes the menu objects used in the launch menu.
            Each menu object is created with its corresponding variables and options.
        """
        self.main_launch_menu = Option_menu_model(
            self.main_menu_variables,
            self.init_render_option_main_launch_menu(),
            ["launch_battle_confirm", "pokedex_menu",
             "manage_team", "save", "quit"],
            (0,0,0),(80,96,176)
        )
        self.display_pokedex_menu = Option_menu_model(
            self.pokedex_menu_variables,
            [],
            None, (255,255,255), (255,255,255),
        )
        self.manage_team_menu = Option_menu_model(
            self.pokedex_menu_variables,
            [],
            None, (255,255,255),(255,255,255),(248,112,48),
        )
        self.confirm_action_menu = Option_menu_model(
            self.confirm_menu_variables,
            self.init_render_option_confirm_choice(),
            None, (0,0,0), (80,96,176)
        )
        self.launch_battle_menu = Option_menu_model(
            self.launch_battle_menu_variables,
            [],
            None, (0,0,0), (0,0,0)
        )
        self.save_menu = Option_menu_model(
            self.save_menu_variables,
            self.init_render_option_save_menu()
        )
    
    def update_menues_objects(self):
        self.main_launch_menu.update_options(
            self.init_render_option_main_launch_menu(),
            margins=self.main_menu_variables
        )
        self.update_manage_team_menu_object()
        self.display_pokedex_menu.update_options(
            self.init_render_option_pokedex(),
            margins=self.pokedex_menu_variables,
            images=self.launch_menu_assets_scaled_dict["pokedex_mini_images"]
        )
        self.confirm_action_menu.update_options(
            self.init_render_option_confirm_choice(),
            margins=self.confirm_menu_variables
        )
        self.launch_battle_menu.update_options(
            self.init_render_option_launch_fight(),
            margins=self.launch_battle_menu_variables,
            images=self.launch_menu_assets_scaled_dict["battle_biomes_box"]
        )
        self.save_menu.update_options(
            self.init_render_option_save_menu(),
            margins=self.save_menu_variables,
        )
    
    def update_manage_team_menu_object(self):
        self.load_team_assets()
        self.launch_menu_assets_scaled_dict.update(
            {"team_mini_images" : self.pre_render_manage_team_mini_images()}
        )
        self.manage_team_menu.update_options(
            self.init_render_option_team(self.player_pokedex.player_team, True),
            margins=self.pokedex_menu_variables,
            images=self.launch_menu_assets_scaled_dict["team_mini_images"]
        )

    def init_render_option_main_launch_menu(self) -> list:
        options : list = [
            self.dialogs["launch"],
            self.dialogs["pokedex"],
            self.dialogs["manage team"],
            self.dialogs["save"],
            self.dialogs["quit"]
        ]
        return options

    def init_render_option_pokedex(self) -> list:
        options : list = []
        for pokemon in self.player_pokedex.pokedex:
            entry = "#" + pokemon
            name = self.dialogs[self.player_pokedex.pokemon_dict[pokemon]["name"]]
            option = entry + " "
            while len(option) + len(name) < 17:
                option += " "
            option += name
            options.append(option)
        return options
    
    def init_render_option_launch_fight(self) -> list:
        options : list = []
        for biome in list(self.player_pokedex.battle_biomes.keys()):
            options.append(self.dialogs[biome])
        return options

    def init_render_option_save_menu(self) -> list:
        options : list = [
            self.dialogs["save_1"],
            self.dialogs["save_2"],
            self.dialogs["save_3"],
            self.dialogs["back"]
        ]
        return options

    def load_assets_launch_menu(self):
        self.launch_menu_assets_dict : dict = {
            "launch_background" : pg.image.load(
                self.GRAPHICS_PATH +"/media/"+\
                "launch screen.png"
            ),
            "pokedex_background" : pg.image.load(
                self.GRAPHICS_PATH +"/media/"+\
                "team select.png"
            )
        }
    
    def _pre_render_assets_launch_menu_(self):
        self.launch_menu_assets_scaled_dict : dict = {
            "launch_background" : pg.transform.scale(
                self.launch_menu_assets_dict["launch_background"], 
                (self.width, self.height)
            ),
            "pokedex_background" : pg.transform.scale(
                self.launch_menu_assets_dict["pokedex_background"],
                (self.width, self.height)
            ),
            "pokedex_mini_images" : self.pre_render_pokedex_mini_images(),
            "battle_biomes_box" : self.pre_render_battle_biomes_images(),
            "team_mini_images" : self.pre_render_manage_team_mini_images()
        }

    def pre_render_manage_team_mini_images(self) -> list:
        rendered_mini_images : list = []
        for image in self.in_game_assets_dict["team_mini_images"]:
            rendered_mini_image = pg.transform.scale(
                image,
                self.mini_image_size
            )
            rendered_mini_images.append(rendered_mini_image)
        return rendered_mini_images
    
    def pre_render_pokedex_mini_images(self) -> list:
        rendered_mini_images : list = []
        for image in self.in_game_assets_dict["pokedex_mini_images"]:
            rendered_image = pg.transform.scale(
                image,
                self.mini_image_size
            )
            rendered_mini_images.append(rendered_image)
        return rendered_mini_images
    
    def pre_render_battle_biomes_images(self) -> list:
        rendered_images : list = []
        for image in self.in_game_assets_dict["battle_biomes_box"]:
            rendered_image = pg.transform.scale(
                image,
                (self.width*0.5, self.height*0.6)
            )
            rendered_images.append(rendered_image)
        return rendered_images

    def draw_launch_menu(self):
        self.screen.blit(
            self.launch_menu_assets_scaled_dict["launch_background"],
            (0,0)
        )
    
    def draw_pokedex_background(self):
        self.screen.blit(
            self.launch_menu_assets_scaled_dict["pokedex_background"],
            (0,0)
        )

    def draw(self):
        """
            init all display related script
        """
        self.draw_launch_menu()
        self.options_menu_draw_dict[self.menu_state]()

    def draw_main_launch_menu(self):
        self.blit_dialog(
            self.dialogs["main menu"],
            self.width*0.032,self.width*0.5,
            self.height*0.3,"midbottom", (0,0,0),True
        )
        self.main_launch_menu.draw_vertical_options()

    def draw_launch_battle_confirm_menu(self):
        self.blit_dialog(
            self.dialogs["confirm battle"],
            self.width*0.032,self.width*0.5,
            self.height*0.3,"midbottom", (0,0,0),True
        )
        self.launch_battle_menu.draw_list_options()
    
    def draw_pokedex_menu(self):
        self.draw_pokedex_background()
        self.display_pokedex_menu.draw_list_options()
        self.draw_pokedex_infos()
        self.draw_focused_pokemon()
    
    def draw_pokedex_infos(self):
        selected_entry = self.player_pokedex.pokemon_dict[
            list(self.player_pokedex.pokemon_dict.keys())[
                int(self.player_pokedex.pokedex[
                    self.display_pokedex_menu.selected_index
                ]) - 1
            ]
        ]
        self.screen.blit(
            pg.transform.scale(
                self.display_pokedex_menu.images[
                    self.display_pokedex_menu.selected_index
                ],
                (self.width*0.28, self.width*0.25)
            ),
            (self.width*0.18, self.height*-abs(0.05))
        )
        self.blit_dialog(
            "#" +\
                selected_entry["entry"],
            self.width*0.027, self.width*0.1, self.height*0.24,
            "bottomleft", bold=True,
        )
        self.blit_dialog(
            self.dialogs[selected_entry["name"]],
            self.width*0.022, self.width*0.196, self.height*0.31,
            bold=True,
        )
        self.blit_dialog(
            self.dialogs["stat attack"] +\
                str(selected_entry["base_attack"]),
            self.width*0.022, self.width*0.06, self.height*0.36,
            "bottomleft"
        )
        self.blit_dialog(
            self.dialogs["stat defense"] +\
                str(selected_entry["base_defence"]),
            self.width*0.022, self.width*0.06, self.height*0.4,
            "bottomleft"
        )
        self.blit_dialog(
            self.dialogs["stat health points"] +\
                str(selected_entry["base_health_points"]),
            self.width*0.022, self.width*0.06, self.height*0.44,
            "bottomleft"
        )
    
    def draw_focused_pokemon(self):
        if self.focused_pokemon != None:
            self.blit_dialog(
                self.dialogs["focused pokemon"],
                self.width*0.022, self.width*0.2, self.height*0.53,
                "midbottom", (255,255,255), True
            )
            self.blit_dialog(
                self.dialogs[
                    self.player_pokedex.pokemon_dict[
                        self.focused_pokemon
                    ]["name"]
                ],
                self.width*0.025, self.width*0.2, self.height*0.57,
                "midbottom", (255,255,255), True
            )
            if self.focused_pokemon ==\
                    self.player_pokedex.pokedex[
                        self.display_pokedex_menu.selected_index
                    ]:
                self.blit_dialog(
                    "#" +\
                        self.player_pokedex.pokemon_dict[self.focused_pokemon]["entry"],
                    self.width*0.027, self.width*0.1, self.height*0.24,
                    "bottomleft", (248,112,48), bold=True,
                )
                self.blit_dialog(
                    self.dialogs[self.player_pokedex.pokemon_dict[self.focused_pokemon]["name"]],
                    self.width*0.022, self.width*0.196, self.height*0.31,
                    color=(248,112,48), bold=True,
                )
                self.blit_dialog(
                    self.dialogs["stat attack"] +\
                        str(self.player_pokedex.pokemon_dict[self.focused_pokemon]["base_attack"]),
                    self.width*0.022, self.width*0.06, self.height*0.36,
                    "bottomleft", (240,176,120)
                )
                self.blit_dialog(
                    self.dialogs["stat defense"] +\
                        str(self.player_pokedex.pokemon_dict[self.focused_pokemon]["base_defence"]),
                    self.width*0.022, self.width*0.06, self.height*0.4,
                    "bottomleft", (240,176,120)
                )
                self.blit_dialog(
                    self.dialogs["stat health points"] +\
                        str(self.player_pokedex.pokemon_dict[self.focused_pokemon]["base_health_points"]),
                    self.width*0.022, self.width*0.06, self.height*0.44,
                    "bottomleft", (240,176,120)
                )

    def draw_manage_team_menu(self):
        self.draw_pokedex_background()
        self.manage_team_menu.draw_picked_list_options()
        self.draw_pokemon_infos()

    def draw_pokemon_infos(self):
        selected_entry = self.player_pokedex.player_team[
            self.manage_team_menu.selected_index
        ]
        self.screen.blit(
            pg.transform.scale(
                self.manage_team_menu.images[
                    self.manage_team_menu.selected_index
                ],
                (self.width*0.28, self.width*0.25)
            ),
            (self.width*0.18, self.height*-abs(0.05))
        )
        self.blit_dialog(
            "#" +\
                selected_entry.entry,
            self.width*0.027, self.width*0.1, self.height*0.24,
            "bottomleft", bold=True,
        )
        self.blit_dialog(
            self.dialogs[selected_entry.name],
            self.width*0.022, self.width*0.196, self.height*0.31,
            bold=True,
        )
        self.blit_dialog(
            self.dialogs["stat attack"] +\
                str(selected_entry.attack),
            self.width*0.022, self.width*0.06, self.height*0.36,
            "bottomleft"
        )
        self.blit_dialog(
            self.dialogs["stat defense"] +\
                str(selected_entry.defense),
            self.width*0.022, self.width*0.06, self.height*0.4,
            "bottomleft"
        )
        self.blit_dialog(
            self.dialogs["stat health points"] +\
                str(selected_entry.health_points),
            self.width*0.022, self.width*0.06, self.height*0.44,
            "bottomleft"
        )

    def draw_save_menu(self):
        self.save_menu.draw_vertical_options()
        self.blit_dialog(
            self.dialogs["save menu"],
            self.width*0.025,
            self.width*0.5, self.height*0.29
        )
    
    def draw_save_confirm_menu(self):
        self.blit_dialog(
            self.dialogs["confirm save"], 
            self.width*0.032, self.width*0.5, self.height*0.3,
            "midbottom", (0,0,0), True
        )
        self.confirm_action_menu.draw_vertical_options()

    def draw_delete_save_confirm_menu(self):
        self.blit_dialog(
            self.dialogs["confirm delete"],
            self.width*0.032, self.width*0.5, self.height*0.3,
            "midbottom", (0,0,0), True
        )
        self.confirm_action_menu.draw_vertical_options()

    def draw_launch_menu_lost_game(self):
        """
            Draws the UI elements related to a lost game state,
            displaying messages about a lost save and how to delete it.
        """
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
        self.blit_dialog(
            self.dialogs["confirm quit"],
            self.width*0.032, self.width*0.5, self.height*0.3,
            "midbottom", (0,0,0), True
        )
        self.confirm_action_menu.draw_vertical_options()