import pygame
import unittest
from ui.button_ui import Buttons


class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        screen_width = 1200
        screen_height = 720
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.rect = Buttons(self.screen)

    def test_rect(self):
        rect = self.rect.make_rect("start game",(200, 200, 190, 40))
        self.assertEqual(rect.height, (40))
        self.assertEqual(rect.width, (190))