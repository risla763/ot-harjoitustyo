import pygame
import random
import time
from objects.rect import ButtonRect
from logic.hiragana_pictures import HiraganaPictureLogic
from ui.button_ui import Buttons
from ui.menu_screen_ui import MenuScreen

class ScoreBoardScreen:
    """Luokka, joka käsittelee pelin ulkonäköön liittyviä asioita ja
    kaikkea koodia, joka liittyy pelin ui:hin.
    Atributes:
        screen: näyttö, jolle peliruudun ui tulee.
    """

    def __init__(self, screen):
        """Konstruktori, jossa määritellään pelissä käytettäviä värejä.
        Args:
            screen: Näyttö, johon pelin ui tulee.
        """
        pygame.init()
        self. pink = (255, 182, 193)
        self.white = (255, 255, 255)
        self.screen = screen

    def scoreboard_screen(self, highest_score):
        """Tässä metodissa on kaikki mitä pelin aikana olevalle näytölle
        piirtyy pelin ajan. Esimerkiksi näytön väri, exit game nappi sekä
        muuta tekstiä"""
        self.screen.fill((255, 204, 229))  
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render(f"{highest_score}", True, (173, 216, 230))
        self.screen.blit(text_surface, (100, 200))


    