import pygame
import unittest
from logic.answers import CheckAndReviev
from logic.hiragana_pictures import HiraganaPictureLogic


class TestInput(unittest.TestCase):
    def setUp(self):
        pygame.init()
        screen_width = 1200
        screen_height = 720
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.hiraganas = HiraganaPictureLogic().list_hiraganas()
        self.user_input = str(self.hiraganas[0][1])
        self.user_input = self.user_input.replace("{", "")
        self.user_input = self.user_input.replace("}", "")
        self.user_input = self.user_input.replace("'", "")
        self.hiragana_tuple = self.hiraganas[0]
        self.user_input_wrong = "1"

    def test_answer_correctly(self):
        answer = CheckAndReviev(self.hiraganas).check_answer(self.hiragana_tuple, self.user_input, self.screen)
        self.assertEqual(answer, (True))

    def test_answer_wrong(self):
        answer = CheckAndReviev(self.hiraganas).check_answer(self.hiragana_tuple, self.user_input_wrong, self.screen)
        self.assertEqual(answer, (False))
