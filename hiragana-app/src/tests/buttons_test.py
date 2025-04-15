import pygame
import unittest
from objects.buttons import Button
from ui.make_rect import Rect


class TestButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.button = Button()
        screen_width = 1200
        screen_height = 720
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.starting_screen = Rect(self.screen)

    def test_rect(self):
        rect = self.starting_screen.make_rect("start game",(200, 200, 190, 40))
        self.assertEqual(rect.height, (40))
        self.assertEqual(rect.width, (190))