import unittest
from korttipakka  import Card
from korttipakka  import Deck
import random
class TestCardDeck(unittest.TestCase):
    def setUp(self):
        print("set up")

    def test_size(self):
        deck =  Deck()
        self.assertEqual(len(deck.cards),52)

    def test_mix(self):
        deck1 = Deck()
        deck2 = Deck()
        random.shuffle(deck2.cards)
        self.assertNotEqual(deck1.cards,deck2.cards)


