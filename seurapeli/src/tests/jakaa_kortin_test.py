import unittest
import pygame
from services.deck_of_cards import Deck

class TestCardDeal(unittest.TestCase):
    def setUp(self):
        print("set up")
        self.deck = Deck()

    def test_deal(self):
        self.deck = Deck()
        self.assertEqual(len(self.deck.cards),52)

    def test_pop(self):
        self.deck.deal()
        self.assertNotEqual(len(self.deck.cards),52)

