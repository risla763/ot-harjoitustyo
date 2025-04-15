import pygame
from objects.buttons import Button
#TÄMÄN LUOKAN NIMEKSI VAIHTUU RECT
class Rect:

    def __init__(self, screen):
        #tässä periin Button luokasta object kansiosta kaikki noi värit yms jututt
        self.screen = screen
        self. pink = (255, 182, 193)
        self.white = (255, 255, 255)

    def make_rect(self, text, position):
        self.start_game_button = Button().make_rect(text,
            self.pink,
            self.white,
            position,
            self.screen
        )
        return self.start_game_button
