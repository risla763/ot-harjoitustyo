import pygame
from objects.buttons import Button

class StartingScreen:

    def __init__(self, screen):
        #tässä periin Button luokasta object kansiosta kaikki noi värit yms jututt
        self.screen = screen

    def make_rect(self):
        self.start_game_button = Button().make_rect("Start game ",
            (255, 182, 193),
            (255, 255, 255),
            (200, 200, 190, 40),
            self.screen
        )
        return self.start_game_button
