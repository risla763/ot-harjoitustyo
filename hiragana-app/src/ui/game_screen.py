import pygame
from objects.buttons import Button

class GameScreen:

    def __init__(self, screen):
        self.screen = screen
        self. pink = (255, 182, 193)
        self.white = (255, 255, 255)

    def make_input_field(self, position):
        #vaihda Button luokassa oeva make_rect nimi, koska näitä metodeja kaksi
        self.start_game_button = Button().make_rect("",
            self.pink,
            self.white,
            position,
            self.screen
        )
        return self.start_game_button
