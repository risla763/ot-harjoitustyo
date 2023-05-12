from services.deck_of_cards import Deck
from services.ui.next_cards import draw_next

"""This method draws the deck on screen"""
def draw_deck(self, surface,deck):
    """Draws a deck of cards on the screen
    Args:
        surface: displays the pygame screen
        deck: a class named deck
        """
    for card in deck.cards:
        pos = (100,100)
        draw_next(surface, pos,card)

