from deck_of_cards import Deck
from ui.next_cards import draw_next

"""This method draws the deck on screen"""
def draw_deck(self, surface,deck):
    for card in deck.cards:
        pos = (100,100)
        draw_next(surface, pos,card)
    return print(enumerate(deck.cards))
