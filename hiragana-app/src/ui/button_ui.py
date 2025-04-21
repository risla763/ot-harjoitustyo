import pygame
from objects.rect import ButtonRect

class Buttons:

    def __init__(self, screen):
        self.screen = screen
        self. pink = (255, 182, 193)
        self.white = (255, 255, 255)

    def make_rect(self, text, position): #kaksi tämän nimistä funktiota koodissa
        self.start_game_button = ButtonRect().make_rect(text,
            self.pink,
            self.white,
            position,
            self.screen
        )
        return self.start_game_button
