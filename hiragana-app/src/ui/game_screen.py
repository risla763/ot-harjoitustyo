import pygame
import random
import time
from objects.rect import ButtonRect
from logic.hiragana_pictures import HiraganaPictureLogic
from ui.button_ui import Buttons
from ui.menu_screen_ui import MenuScreen

class GameScreen:
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

    def game_screen(self):
        """Tässä metodissa on kaikki mitä pelin aikana olevalle näytölle
        piirtyy pelin ajan. Esimerkiksi näytön väri, exit game nappi sekä
        muuta tekstiä"""
        self.screen.fill((255, 204, 229))  
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render("", True, (173, 216, 230))
        self.exit_game_button(self.screen)
        self.screen.blit(text_surface, (100, 200))

    def draw_hiragana(self, hiraganas): 
        """Tämä metodi piirtää hiraganat näytölle. 
        Args: 
            hiraganas: lista, jossa tupleja, jotka sisältävät hiraganat ja niitä vastaavt tavut.
        Returns: 
            hiragana_tuple: palauttaa tuplen, joka sisältää tässä kohdassa näytöllä olevan
            hiraganan kuvan, sekä sitä vastaavan tavun.
        """
        hiragana_rect = ButtonRect().make_rect("",self.pink, self.pink,(530,100, 130, 120), self.screen)
        #tässä logiikkaa, joka pitää siirtää logiikka osioon
        hiragana_tuple = random.choice(hiraganas)
        image = hiragana_tuple[0]
        self.screen.blit(image,(530,100)) 
        pygame.display.flip()
        return hiragana_tuple

    def make_input_field(self, position, screen):
        """Tämä piirtää näytölle laatikon, jonka sisällä näkyy
        käyttäjän kirjoittama teksti.
        Args:
            position: mihin suorakulmio tulee näytöllä
            screen: näyttö, johon suorakulmio tulee.
        Returns:
            self.input_field: laatikko, johon käyttäjän kirjoittama teksti tulee.
        """
        #vaihda button rect kansion nimeä!!!!
        self.input_field = ButtonRect().make_rect("",
            self.pink,
            self.white,
            position,
            screen
        )
        return self.input_field

    def exit_game_button(self, screen):
        """metodi, joka kutsuu Buttons luokkaa piirtämään exit game- nimisen napin
        Args: 
            näyttö jolle nappi tulee.
        Returns:
            palauttaa exit game -napin.
        """
        return Buttons(screen).make_rect("Exit game",(700, 200, 200, 40))

    def comment_ui_right(self, answer, syllable):
        #tämä metodi ei tarvitse syllable muuttujaa!
        """metodi, joka kutsuu ButtonRect luokkaa piirtämään suorakulmion,
        jonka sisälle tulee "correct" jos käyttäjä saa arvattua oikein.
        Args: 
            answer: vastaus, joka on True, jos käyttäjä on saanut arvattua oikein ja muuten False
            syllable: tavu, joka on oikea vastaus (atm turha)
            
        Returns:
            palauttaa suorakulmion, jonka sisälle tulee teksti "correct"
        """
        hiragana_rect = ButtonRect().make_rect("Correct!",self.white, self.pink,(510,0, 110, 50), self.screen)

    def comment_ui_wrong(self, answer, syllable):
        """metodi, joka kutsuu ButtonRect luokkaa piirtämään suorakulmion,
        jonka sisälle tulee teksti, jossa kerrotaan että
        väärin meni ja oikea vastaus
        Args: 
            answer: vastaus, joka on False, jos käyttäjä ei ole arvannut oikein, muuten True
            syllable: tavu, joka on oikea vastaus
            
        Returns:
            palauttaa suorakulmion, jonka sisällä lukee "wring answer" yms.
        """
        hiragana_rect = ButtonRect().make_rect((f"Wrong, answer is: {syllable}"),self.white, self.pink,(510,0, 330, 50), self.screen)

    def clear_comment_field(self):
        hiragana_rect = ButtonRect().make_rect("",self.white, (255, 204, 229),(510,0, 330, 50), self.screen)

