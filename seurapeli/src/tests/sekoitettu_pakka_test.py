import unittest
from services.card_deck import Card
from services.deck_of_cards import Deck
import random


class TestCardDeck(unittest.TestCase):
    def setUp(self):
        print("set up")

    def test_size(self):
        deck = Deck()
        self.assertEqual(len(deck.self.cards), 52)

    def test_mix(self):
        deck1 = Deck().self.cards()
        deck2 = Deck().self.cards()
        random.shuffle(deck2.cards)
        self.assertNotEqual(deck2, deck1)

