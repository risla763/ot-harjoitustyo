import pygame
import random

class HiraganaUi:
    #poista

    def __init__(self, screen):
        pygame.init()
        self.screen = screen

    def draw_hiragana(self): 
        #palauttaa random hiraganan listasta
        self.tuple_list = random.choice(self.tuple_list)
        hiragana_tuple[0]
        #letter_tuple[1] --> oikea vastaus
        image = hiragana_tuple[0]
        self.screen.blit(image,(0,0))
        pygame.display.flip()
        #voisko tää palauttaa oikean vastauksen
    
    def tuple_hiragana_list(self, hiraganas):
        self.tuple_list = hiraganas
        return self.tuple_list
        
