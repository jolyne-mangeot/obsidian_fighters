import pygame as pg

class Game_menues_sounds:
    """
    This class handles the initialization of various sounds in the game, including Pokémon cries and in-game sounds
    """
    def init_game_menu_sounds(self):
        self.load_musics_launch_menu()
    
    def load_musics_launch_menu(self):
        self.launch_menu_musics_dict : dict = {
            "launch_menu" : pg.mixer.Sound(self.MUSIC_PATH + "launch_menu_sound_track.mp3"),
            "launch_menu_night" : pg.mixer.Sound(self.MUSIC_PATH + "launch_menu_night_sound_track.wav"),
            "new_game" : pg.mixer.Sound(self.MUSIC_PATH + "new_game_sound_track.wav")
        }

    def init_in_battle_sounds(self):
        """
        Initialize sound effects for in-game actions, such as leveling up
        """
        self.load_player_pokemons_cry()
        self.load_enemy_pokemons_cry()
        self.load_sounds_in_battle()
        self.loads_musics_in_battle()

    def loads_musics_in_battle(self):
        self.in_battle_musics = {
            "caught pokemon" : pg.mixer.Sound(self.SFX_PATH + "caught-a-pokemon.mp3"),
            "wild battle" : pg.mixer.Sound(self.MUSIC_PATH + "wild_battle_sound_track.wav"),
            "wild battle intro" : pg.mixer.Sound(self.MUSIC_PATH + "wild_battle_sound_intro.wav"),
            "trainer battle" : pg.mixer.Sound(self.MUSIC_PATH + "trainer_battle_sound_track.mp3"),
            "gym battle" : pg.mixer.Sound(self.MUSIC_PATH + "gym_battle_sound_track.mp3"),
            "victory" : pg.mixer.Sound(self.MUSIC_PATH + "victory_sound_track.wav"),
            "evolving" : pg.mixer.Sound(self.MUSIC_PATH + "evolving_sound_track.mp3")
        }
    
    def load_sounds_in_battle(self):
        self.in_game_actions_sounds = {
            "heal" : pg.mixer.Sound(self.SFX_PATH + "heal.wav"),
            "pokeball throw" : pg.mixer.Sound(self.SFX_PATH + "pokeball throw.wav"),
            "pokeball wobble" : pg.mixer.Sound(self.SFX_PATH + "pokeball shaking sounds.ogg"),
            "statup" : pg.mixer.Sound(self.SFX_PATH + "stat-up.wav"),
            "levelup" : pg.mixer.Sound(self.SFX_PATH + "level_up.mp3"),
            "run away" : pg.mixer.Sound(self.SFX_PATH + "run-away.mp3"),
            "pokemon out" : pg.mixer.Sound(self.SFX_PATH + "pokemon-out.mp3"),
            "low health" : pg.mixer.Sound(self.SFX_PATH + "low_hp_pokemon.mp3"),
            "hit no effective" : pg.mixer.Sound(self.SFX_PATH + "hit_no_effective.mp3"),
            "hit not very effective" : pg.mixer.Sound(self.SFX_PATH + "hit_weak_not_very_effective.mp3"),
            "hit very effective" : pg.mixer.Sound(self.SFX_PATH + "hit_super_effective.mp3 ")
        }

    def load_player_pokemons_cry(self):
        """
        Initialize Pokémon cry sounds based on the player's team
        """
        for pokemon in self.player_pokedex.player_team:
            cry_path : str = self.GRAPHICS_PATH + "pokemon/" + pokemon.entry + "/cry.ogg"
            pokemon.sound = pg.mixer.Sound(cry_path)
    
    def load_evolved_pokemon_cry(self):
        pokemon = self.battle.active_pokemon
        cry_path : str = self.GRAPHICS_PATH + "pokemon/" + pokemon.entry + "/cry.ogg"
        pokemon.sound = pg.mixer.Sound(cry_path)
    
    def load_enemy_pokemons_cry(self):
        for pokemon in self.battle.enemy_team:
            cry_path : str = self.GRAPHICS_PATH + "pokemon/" + pokemon.entry + "/cry.ogg"
            pokemon.sound = pg.mixer.Sound(cry_path)

    def play_enemy_pokemon_cry(self):
        self.double_effects_channel.play(self.battle.enemy_pokemon.sound)

    def play_active_pokemon_cry(self):
        self.double_effects_channel.play(self.battle.active_pokemon.sound)