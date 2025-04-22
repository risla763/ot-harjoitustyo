import pygame
from objects.rect import ButtonRect
#tämä button ui luokka mutta erikseen rect muodostus luokka

class Buttons:
    """Tämä luokka määrittää nappien ulkonäön."""

    def __init__(self, screen):
        """Luokan konstruktori, jossa määritellään värejä, joita pelin napeissa
        käytetään.
        Args: 
            screen: pelin näyttö
        """
        self.screen = screen
        self. pink = (255, 182, 193)
        self.white = (255, 255, 255)

    def make_rect(self, text, position): #kaksi tämän nimistä funktiota koodissa
        """Kutsuu suorakulmion tekokoodia, joka tekee napin ruudulle
            Returns:
                self.start_game_button: palauttaa napin
        """
        self.start_game_button = ButtonRect().make_rect(text,
            self.pink,
            self.white,
            position,
            self.screen
        )
        return self.start_game_button
