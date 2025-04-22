import pygame
import unittest
from logic.answers import CheckAndReviev
from logic.hiragana_pictures import HiraganaPictureLogic


class TestInput(unittest.TestCase):
    def setUp(self):
        self.hiraganas_1 = HiraganaPictureLogic().list_hiraganas()
        self.hiraganas_2 = HiraganaPictureLogic().list_hiraganas()

    def test_shuffles_correctly(self):
        self.assertNotEqual(self.hiraganas_1, self.hiraganas_2)
