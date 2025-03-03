import pygame as pg

from game.control.models_controller import Models_controller

class Game_menues_display:
    """
        This class handles the display of various game menus, initialization of in-game display elements, 
        and the loading of graphical assets like Pokémon images and combat screens.
    """
    @classmethod
    def init_in_game_display(cls):
        """
            Initializes the in-game display, root variables, and loads the graphics for both launch menus and Pokémon.
        """
        cls.load_in_game_assets()
    
    @classmethod
    def load_in_game_assets(cls):
        cls.in_game_assets_dict : dict = {
            "pokedex_mini_images" : cls.load_pokedex_mini_images(),
            "battle_biomes_box" : cls.load_battle_biomes_images()
        }
        cls.load_team_assets()
    
    @classmethod
    def load_team_assets(cls):
        Game_menues_display.in_game_assets_dict.update({
            "team_mini_images" : cls.load_manage_team_mini_images(),
            "team_back_image" : cls.load_player_pokemons()
        })

    @classmethod
    def load_manage_team_mini_images(cls) -> list:
        mini_images : list = []
        for pokemon in Models_controller.player_pokedex.player_team:
            mini_image = cls.in_game_assets_dict[
                "pokedex_mini_images"
            ][
                Models_controller.player_pokedex.pokedex.index(pokemon.entry)
            ]
            mini_images.append(mini_image)
        return mini_images

    @staticmethod
    def load_player_pokemons() -> list:
        """
            Loads and scales the graphics for the Pokémon in the player's team, 
            including their back images.
        """
        back_images : list = []
        for pokemon in Models_controller.player_pokedex.player_team:
            back_image = pg.image.load(
                Models_controller.GRAPHICS_PATH + "pokemon/" +\
                pokemon.entry + "/back.png"
            )
            back_images.append(back_image)
        return back_images

    @staticmethod
    def load_pokedex_mini_images() -> list:
        mini_images : list = []
        for pokemon in Models_controller.player_pokedex.pokedex:
            mini_image = pg.image.load(
                Models_controller.GRAPHICS_PATH +"pokemon/"+pokemon+"/mini.png"
            )
            mini_images.append(mini_image)
        return mini_images

    @staticmethod
    def load_battle_biomes_images() -> list:
        images : list = []
        for biome in list(Models_controller.player_pokedex.battle_biomes.keys()):
            image = pg.image.load(
                Models_controller.GRAPHICS_PATH+"biomes variants/"+\
                "launch_" + biome + "_box.png"
            )
            images.append(image)
        return images

    def init_render_option_team(self, team, forced_switch=False, team_full=False, menu="in_battle"):
        """
            Prepares a list of options for rendering the player's team selection. 
            It includes options for each Pokémon in the team, and possibly an option to go back.
        """
        options = []
        for pokemon in team:
            options.append(self.dialogs[pokemon.name])
            level_display = self.dialogs["lvl"] + str(int(pokemon.level))
            while len(options[-1]) + len(level_display) < (25 if menu == "launch_menu" else 16):
                options[-1] += " "
            options[-1] += level_display

        while len(options) < 6 and not forced_switch and not team_full:
            options.append("")
        if not forced_switch and not team_full:
            options.append(self.dialogs['back'])
        return options

    def _load_graphics_combat_(self):
        self.pokemon_ground_img=pg.image.load(
            self.GRAPHICS_PATH+"biomes variants/"+\
            "battle_"+self.battle.battle_biome["name"]+"_ground.png"
        )
        self.pokemon_ground_img=pg.transform.scale(
            self.pokemon_ground_img,
            (self.width*0.31,self.width*0.116)
        )
        self.active_pokemon_ground_img=pg.transform.scale(
            self.pokemon_ground_img,
            (self.width*0.523,self.width*0.196)
        )
        self.pokeball_img=pg.image.load(
            self.GRAPHICS_PATH+"/media/"+\
            "pokeball_sprite.png"
        )
        self.pokeball_img=pg.transform.scale(
            self.pokeball_img,
            (self.width*0.02, self.width*0.02)
        )
        self.pokeball_caught_img=pg.image.load(
            self.GRAPHICS_PATH+"/media/"+\
            "pokeball_sprite_caught.png"
        )
        self.pokeball_caught_img=pg.transform.scale(
            self.pokeball_caught_img,
            (self.width*0.02, self.width*0.02)
        )
        self.text_box_empty=pg.image.load(
            self.GRAPHICS_PATH+"/media/"+\
            "textbox pre combat.png"
        )
        self.text_box_empty=pg.transform.scale(
            self.text_box_empty,
            (self.width,self.height*0.35)
        )
        self.action_bg_img=pg.image.load(
            self.GRAPHICS_PATH+"biomes variants/"+\
            "battle_"+self.battle.battle_biome["name"]+"_background.jpg"
        )
        self.action_bg_img=pg.transform.scale(
            self.action_bg_img,
            (self.width,self.height)
        )
        self.action_box=pg.image.load(
            self.GRAPHICS_PATH+"/media/"+\
            "textbox_combat.png"
        )
        self.action_box=pg.transform.scale(
            self.action_box,
            (self.width, self.height*0.35)
        )

        self.pkmn_info_box_enemy=pg.image.load(self.GRAPHICS_PATH+"/media/"+"pkmn info enemy.png")
        self.pkmn_info_box_enemy=pg.transform.scale(self.pkmn_info_box_enemy,(self.width*0.47,self.height*0.23))

        self.pkmn_info_box_player=pg.image.load(self.GRAPHICS_PATH+"/media/"+"pkmn info player.png")
        self.pkmn_info_box_player=pg.transform.scale(self.pkmn_info_box_player,(self.width*0.47,self.height*0.23))

        self.action_box=pg.image.load(self.GRAPHICS_PATH+"/media/"+"textbox_combat.png")
        self.action_box=pg.transform.scale(self.action_box,(self.width, self.height*0.35))

    def _enemy_pokemon_load_(self):
        """
            Loads and scales the front-facing images for the enemy Pokémon team.
            Images are loaded from the specified path and resized to fit the defined dimensions.
        """
        for pokemon in self.battle.enemy_team:
            front_image = pg.image.load(self.GRAPHICS_PATH + "pokemon/" + pokemon.entry + "/front.png")
            pokemon.front_image = pg.transform.scale(front_image, self.enemy_pokemon_image_size)

    def load_evolution_combat(self):
        back_image = pg.image.load(
            self.GRAPHICS_PATH + "pokemon/" +\
            self.battle.active_pokemon.entry + "/back.png"
        )
        self.battle.active_pokemon.back_image = pg.transform.scale(
            back_image, 
            self.active_pokemon_image_size
        )
    
    def draw_action_background(self):
        self.screen.blit(
            self.action_bg_img,
            (0,0)
        )

    def draw_pokeball_thrown(self):
        self.screen.blit(
            self.pokeball_img,
            (self.width*0.761, self.height*0.251)
        )
    
    def draw_pokeball_caught(self):
        self.screen.blit(
            self.pokeball_caught_img,
            (self.width*0.761, self.height*0.251)
        )

    def draw_dialogue_box(self):
        self.text_box_empty=pg.transform.scale(self.text_box_empty, (self.width,self.height*0.35))
        self.screen.blit(
            self.text_box_empty,
            (0,self.height*0.65)
        )
    
    def draw_action_box(self):
        self.action_box=pg.transform.scale(self.action_box,(self.width*0.22, self.height*0.4))
        self.screen.blit(
            self.action_box,
            (self.width*0.687,self.height*0.62)
        )

    def draw_pkmn_info_box_enemy(self):
        self.screen.blit(
            self.pkmn_info_box_enemy,
            (self.width*0.05,0)
        )
    
    def draw_pkmn_info_box_player(self):
        self.screen.blit(
            self.pkmn_info_box_player,
            (self.width*0.52,self.height*0.4222)
        )