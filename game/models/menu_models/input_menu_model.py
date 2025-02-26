import pygame as pg
import string

from game.control.models_controller import Models_controller

class Input_menu_model(Models_controller):
    """
    A class for handling user text input in a menu.
    Inherits from the Display class.
    """
    def __init__(self,
            margins : tuple, dialog : str,
            color=(0,0,0), image=False):
        """
        Initializes the input menu model.
        """
        self.from_left, self.from_top = margins
        self.dialog = dialog
        self.input = ""
        self.input_color = color
        self.image = image
        self.pre_render()
    
    def pre_render(self):
        Models_controller.__init__(self)
        self.rendered_input = self.pixel_font_menu_deselected.render(self.dialog + self.input, True, self.input_color)
        self.rendered_input_rect = self.rendered_input.get_rect(center=(self.from_left, self.from_top))
    
    def draw_input(self):
        self.screen.blit(self.rendered_input, self.rendered_input_rect)

    def get_event_input(self, event):
        """
        Handles user keyboard input
        """
        if event.type == pg.KEYDOWN:
            self.effects_channel.play(self.menues_sounds["cursor move"])

            if event.key == pg.K_BACKSPACE and self.input != "":
                self.input = self.input[:-1]
                self.pre_render()

            elif len(self.input) <= 9:
                if str(event.unicode).upper() in string.ascii_uppercase or event.unicode in (" ", "-", "'"):
                    self.input += event.unicode
                    self.pre_render()