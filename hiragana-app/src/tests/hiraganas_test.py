import pygame
import unittest
from logic.answers import CheckAndReviev
from logic.hiragana_pictures import HiraganaPictureLogic
from ui.game_screen import GameScreen


class TestInput(unittest.TestCase):
    """Testaa käyttäjän syöttämää tekstiä"""
    def setUp(self):
        self.hiraganas_1 = HiraganaPictureLogic().list_hiraganas()
        self.hiraganas_2 = HiraganaPictureLogic().list_hiraganas()
        screen_width = 1200
        screen_height = 720
        self.screen = pygame.display.set_mode((screen_width,screen_height))

    def test_shuffles_correctly(self):
        #siirrä tämä eri testi tiedostoon
        """Testaa sekoittaako pakan oikein"""
        self.assertNotEqual(self.hiraganas_1, self.hiraganas_2)

    def test_draw_random_hiragana(self): 
        """Testaa onko randomilla arvottu tuple listassa jossa on kaikki vastaukset"""
        hiraganas = HiraganaPictureLogic().list_hiraganas()
        tuple = GameScreen(self.screen).draw_hiragana(hiraganas)
        works = False
        if tuple in hiraganas:
            works = True
        self.assertEqual(works, (True))
        #tähän viel se testi että vastaus ei oo listassa