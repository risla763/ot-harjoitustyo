import pygame
import random
import os
from PIL import Image

class Card:
    def __init__(self, suit, rank, cards): #yksittäinen kortti
        self.suit = suit #väri
        self.rank = rank #arvo
        #cards.append(suit,rank) 
        #liitä kuvat tuple listassa oleviin arvoihin:
        png_directory = "Playing Cards/PNG-cards-1.3"

        file = os.path.join(png_directory, f"{rank}_of_{suit}.png")
        self.image = pygame.image.load(file)


        #self.image = pygame.image.load("Playing Cards/PNG-cards-1.3/2_of_clubs.png") #kuva jostain (surface of the card) #vanha: (f"cards/{rank}_{suit}.png")
        self.rect = self.image.get_rect()
        #for card in cards:
            #yhdistä kuva tupleen:
            #file = os.path.join(png_directory, f"{rank}_of_{suit}.png")
            #self.image = pygame.image.load(file)


        #self.image = pygame.image.load("Playing Cards/PNG-cards-1.3/2_of_clubs.png") #kuva jostain (surface of the card) #vanha: (f"cards/{rank}_{suit}.png")
            #self.rect = self.image.get_rect() #suorakaiteen muotinen objekti joka esittää korttia ruudulla (auttaa liikuttamaan kuvaa)
            #print(self.rect)
    def draw(self, surface, pos): #surface on näyttö , jolle kortti vedetään
        #print(self.suit)
        #print(self.rank)
        
        self.rect.topleft = pos #tuple, joka sisältää koordinaatit kortin vasemmasta yläkulmasta
        surface.blit(self.image, self.rect) #rect kertoo mihin näytöllä se kortti vedetään
        # tähän metodiin tarvitaan kolme kertaa nosto pakasta ja että ruudulle ilmestyy kolme korttia eri koordinaatteihin

class Deck: #korttipakka
    def __init__(self):
        self.cards = []
        suits = ['spades', 'hearts', 'diamonds', 'clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        for suit in suits: #värit
            for rank in ranks: #arvot
                card = Card(suit, rank, self.cards) #yksittäinen kortti (TUPLE)
                self.cards.append(card) #tuple lista korteista
        random.shuffle(self.cards) #sekoitetaan pakkaa

    def draw(self, surface, pos): #piirtää koko pakan
        a = 300
        i = 0
        for n,card in enumerate(self.cards): #i on indeksi (kuinka mones) mutta loopissa toimitaan tuplejen kanssa #i, 
            print(i)
            if i >= 50:
                card.draw(surface, (a,100))
                a += 800
            else:
                card.draw(surface, (100,100)) #tämä pistää kortin kuvan näytölle (x,y) #(pos[0] + i * 20, pos[1]) koritit levitettyinä #piirrä kolme viimeistä levitettyinä
                #tämä pistää kortin kuvan näytölle (x,y) #(pos[0] + i * 20, pos[1]) koritit levitettyinä #piirrä kolme viimeistä levitettyinä
            i += 1
    def deal(self):
        return self.cards.pop() #poistaa kierroksella jaetun kortin (tähän pitää myös saada aikaiseksi se, että niitä on kolme)

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 1800
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Card Deck")

# Create a deck of cards
deck = Deck()

# Draw the deck of cards PIIRTÄÄ KORTTIPAKAN
deck.draw(screen, (100, 100))

# Deal a card and draw it on the screen #yksittäinen kortti
card = deck.deal()
#card.draw(screen, (200, 100)) #piirrä tämä siihen kohtaan

# Update the display
pygame.display.update()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
