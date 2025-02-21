import pygame as pg

from game.views.sounds import Sounds

class Game_menues_sounds(Sounds):
    """
    This class handles the initialization of various sounds in the game, including Pokémon cries and in-game sounds
    """
    def init_in_game_sounds(self):
        Sounds.__init__(self)
        self.init_sounds()
        self.init_pokemons_cry()
    
    def init_game_menu_sounds(self):
        Sounds.__init__(self)
        self.init_sounds()
        self.init_launch_menu_musics()
    
    def init_launch_menu_musics(self):
        self.launch_menu_musics_dict : dict = {
            "launch_menu" : pg.mixer.Sound(self.MUSIC_PATH + "launch_menu_sound_track.mp3"),
            "launch_menu_night" : pg.mixer.Sound(self.MUSIC_PATH + "launch_menu_night_sound_track.wav"),
        }

    def init_pokemons_cry(self):
        """
        Initialize Pokémon cry sounds based on the player's team
        """
        for pokemon in self.player_pokedex.player_team:
            cry_path : str = self.GRAPHICS_PATH + "pokemon/" + pokemon.entry + "/cry.ogg"
            pokemon.sound = pg.mixer.Sound(cry_path)
    
    def init_evolved_pokemon_cry(self):
        pokemon = self.battle.active_pokemon
        cry_path : str = self.GRAPHICS_PATH + "pokemon/" + pokemon.entry + "/cry.ogg"
        pokemon.sound = pg.mixer.Sound(cry_path)
    
    def init_enemy_pokemons_cry(self):
        for pokemon in self.battle.enemy_team:
            cry_path : str = self.GRAPHICS_PATH + "pokemon/" + pokemon.entry + "/cry.ogg"
            pokemon.sound = pg.mixer.Sound(cry_path)

    def play_enemy_pokemon_cry(self):
        self.double_effects_channel.play(self.battle.enemy_pokemon.sound)

    def play_active_pokemon_cry(self):
        self.double_effects_channel.play(self.battle.active_pokemon.sound)

    def init_in_battle_sounds(self):
        """
        Initialize sound effects for in-game actions, such as leveling up
        """
        self.init_in_game_sounds()
        self.init_enemy_pokemons_cry()
        self.init_battle_actions_sounds()
        self.init_battle_music()
    
    def init_battle_music(self):
        self.in_battle_musics = {
            "caught pokemon" : pg.mixer.Sound(self.SFX_PATH + "caught-a-pokemon.mp3"),
            "wild battle" : pg.mixer.Sound(self.MUSIC_PATH + "wild_battle_sound_track.wav"),
            "wild battle intro" : pg.mixer.Sound(self.MUSIC_PATH + "wild_battle_sound_intro.wav"),
            "trainer battle" : pg.mixer.Sound(self.MUSIC_PATH + "trainer_battle_sound_track.mp3"),
            "gym battle" : pg.mixer.Sound(self.MUSIC_PATH + "gym_battle_sound_track.mp3"),
            "victory" : pg.mixer.Sound(self.MUSIC_PATH + "victory_sound_track.wav"),
            "evolving" : pg.mixer.Sound(self.MUSIC_PATH + "evolving_sound_track.mp3")
        }
    
    def init_battle_actions_sounds(self):
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
