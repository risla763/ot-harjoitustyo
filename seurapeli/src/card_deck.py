import os
import pygame

"""This class makes a png image its own variable."""
class Card:
    def __init__(self, suit, rank, cards): #yksittäinen kortti
        self.suit = suit #väri
        self.rank = rank #arvo
        self.cards = cards
        png_directory = "PNG-cards-1.3"
        file = os.path.join(png_directory, f"{rank}_of_{suit}.png")
        self.image = pygame.image.load(file)
        self.list_of_ranks = []
        self.list_of_ranks.append(rank)
        #print(self.list_of_ranks)
        self.rect = self.image.get_rect()
    def get_rank(self):
        """This method returns the rank of the card
        that is in the png image."""
        return self.rank
    def get_suit(self):
        """This returns the suit of the card that is in the ong image."""
        return self.suit
