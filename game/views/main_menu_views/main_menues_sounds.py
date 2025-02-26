import pygame as pg

class Main_menues_sounds:
    def init_main_menues_sounds(self):
        self.load_musics_main_menues()
    
    def load_musics_main_menues(self):
        self.main_menues_musics : dict = {
            "title_screen" : pg.mixer.Sound(self.MUSIC_PATH + "title_screen_sound_track.mp3"),
        }