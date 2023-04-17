import pygame
import random
import os
from PIL import Image
import time
#from main import Main
from pygame.locals import *
import sys

class Card:
    def __init__(self, suit, rank, cards): #yksittäinen kortti
        self.suit = suit #väri
        self.rank = rank #arvo
        #cards.append(suit,rank) 
        #liitä kuvat tuple listassa oleviin arvoihin:
        png_directory = "Playing Cards/PNG-cards-1.3"

        file = os.path.join(png_directory, f"{rank}_of_{suit}.png")
        self.image = pygame.image.load(file)

        self.list_of_ranks = []
        self.list_of_ranks.append(rank)
        #print(self.list_of_ranks)
 
        #self.image = pygame.image.load("Playing Cards/PNG-cards-1.3/2_of_clubs.png") #kuva jostain (surface of the card) #vanha: (f"cards/{rank}_{suit}.png")
        self.rect = self.image.get_rect()
        #for card in cards:
            #yhdistä kuva tupleen:
            #file = os.path.join(png_directory, f"{rank}_of_{suit}.png")
            #self.image = pygame.image.load(file)
        #print(self.rank)
    def get_rank(self):
        return self.rank

        #self.image = pygame.image.load("Playing Cards/PNG-cards-1.3/2_of_clubs.png") #kuva jostain (surface of the card) #vanha: (f"cards/{rank}_{suit}.png")
            #self.rect = self.image.get_rect() #suorakaiteen muotinen objekti joka esittää korttia ruudulla (auttaa liikuttamaan kuvaa)
            #print(self.rect)
    def draw(self, surface, pos): #surface on näyttö , jolle kortti vedetään
        #print(self.suit)
        #print(self.rank)
        
        self.rect.topleft = pos #tuple, joka sisältää koordinaatit kortin vasemmasta yläkulmasta (x,y)
        surface.blit(self.image, self.rect) 
        
        #print(self.rank)
