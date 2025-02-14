import pygame as pg
from control.states_control import States

pg.font.init()

class In_fight(States):
    def __init__(self):
        States.__init__(self)

    def cleanup(self):
        # cleans up all menu related data
        pass

    def startup(self):
        # initiates all menu related data
        # init new fight instance
        self.player_team : list = self.player_pokedex.player_team.copy()
        self.enemy_team : list = "a"

    def get_event(self, event):
        # all input checks for in GAME
        if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYDOWN:
            self.done = True
        
    def update(self):
        self.draw()
    
    def draw(self):
        self.screen.fill((0,0,255))