import pygame
import random
import time
from objects.rect import ButtonRect
from logic.hiragana_pictures import HiraganaPictureLogic
from ui.hiragana import HiraganaUi

class GameScreen:

    def __init__(self, screen):
        self. pink = (255, 182, 193)
        self.white = (255, 255, 255)
        self.screen = screen

    def game_screen(self):
        #TÄHÄN KAIKKI MITÄ GAME SCREENILLE PIIRTYY JA PYSYY KOKO PELIN AJAN
        self.screen.fill((255, 204, 229))  
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render("Game comes here", True, (173, 216, 230))
        self.screen.blit(text_surface, (100, 200))

    def draw_hiragana(self, hiraganas): 
        hiragana_rect = ButtonRect().make_rect("",self.pink, self.pink,(530,100, 130, 120), self.screen)
        hiragana_tuple = random.choice(hiraganas)
        image = hiragana_tuple[0]
        self.screen.blit(image,(530,100)) 
        pygame.display.flip()
        return hiragana_tuple

    def make_input_field(self, position, screen):
        #vaihda button rect kansion nimeä!!!!
        self.start_game_button = ButtonRect().make_rect("",
            self.pink,
            self.white,
            position,
            screen
        )
        return self.start_game_button

#tämä on logiikkaa eli logiikka osioon...
    def comment_if_correct(self, answer, syllable):
        ticks=pygame.time.get_ticks()
        i = 0
        if answer == True:
            while i < 60:
                ticks=pygame.time.get_ticks()
                #vaihda fontti yms...mutta tuolla ui metodissa vaihda
                hiragana_rect = ButtonRect().make_rect("Oikein",self.white, self.pink,(510,0, 110, 50), self.screen)
                i = i+1
        else:
            while i < 200:
                ticks=pygame.time.get_ticks()
                hiragana_rect = ButtonRect().make_rect((f"Väärin, vastaus: {syllable}"),self.white, self.pink,(510,0, 330, 50), self.screen)
                i = i+1
                #tähän että pitää kirjoittaa uudelleen ja vasta sitten seuraava vaihtuu
        hiragana_rect = ButtonRect().make_rect("",self.white, (255, 204, 229),(510,0, 330, 50), self.screen)
    # printing th