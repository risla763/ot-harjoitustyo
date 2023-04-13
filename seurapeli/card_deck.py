import pygame
import random
import os
from PIL import Image
import time
import sys
from korttipakka import Card





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




class Deck: #korttipakka
    def __init__(self):
        self.cards = []
        suits = ['spades', 'hearts', 'diamonds', 'clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
        for suit in suits: #värit
            for rank in ranks: #arvot
                card = Card(suit, rank, self.cards) #yksittäinen kortti (TUPLE) tässä hypätään ylempään luokkaan
                self.cards.append(card) #tuple lista korteista
        random.shuffle(self.cards) #sekoitetaan pakkaa

    def draw(self, surface, pos): #piirtää koko pakan
        self.list_of_three_cards = []
        a = 650
        #a = 100
        i = 0
        for n,card in enumerate(self.cards): #i on indeksi (kuinka mones) mutta loopissa toimitaan tuplejen kanssa #i, 
            #if i >= 50:
                #card.draw(surface, (a,100))
                #a = 650
                #a += 550
                #list_of_three_cards.append(card)
            #else:
                card.draw(surface, (100,100)) #tämä pistää kortin kuvan näytölle (x,y) #(pos[0] + i * 20, pos[1]) koritit levitettyinä #piirrä kolme viimeistä levitettyinä
                #tämä pistää kortin kuvan näytölle (x,y) #(pos[0] + i * 20, pos[1]) koritit levitettyinä #piirrä kolme viimeistä levitettyinä
                #if i == 50:
                self.list_of_three_cards.append(card)
            #i += 1
        return print(enumerate(self.cards))
    def deal(self):
        return self.cards.pop() #poistaa ja palauttaa? kierroksella jaetun kortin (tähän pitää myös saada aikaiseksi se, että niitä on kolme)
    
    def next_card(self, screen,card_positions):
        every_card = len(self.cards)

        card = self.cards.pop()
        card_rect = card.draw(screen, card_positions) #menee Card luokan draw metodiin


        #kutsutaan samaa korttia uudestaan, että saadaan rank
        #NUMERO LASKURI TÄHÄN, KOSKA TÄMÄ METODI PERII RUUDUN
        self.num = card.get_rank()
        #self.old_rank = card.get_rank()
        
        #final_num = self.num + final_num
        #font = pygame.font.SysFont(None, 77) 
        #num_surface = font.render(str(self.num),True,(0,0,0))
        #input_rect2 = pygame.Rect(1000,890,493,60)
        #screen.blit(num_surface,input_rect2) #tällä pitäisi saada teksti näytölle
        #pygame.draw.rect(screen,(0,0,0),input_rect2,2)
        #pygame.display.flip() 
        #print(self.num)

        
    def count(self, screen,count):
        if count <= 3:
            final_num = 0 #tähän tarvitaan pinossa päällimmäisen kortin rankki
        else:
            final_num = self.fin
        if self.num == "king":
            self.num = "13"
        elif self.num == "queen":
            self.num = "12"
        elif self.num == "jack":
            self.num = "11"
        elif self.num == "ace":
            self.num  = "14"
        final_num += int(self.num)
        font = pygame.font.SysFont(None, 77) 
        num_surface = font.render(str(final_num),True,(40,40,40))
        self.fin = final_num
        input_rect2 = pygame.Rect(100,890,40,60)
        input_rect2_surface = screen.subsurface(input_rect2) #estää numeroiden menemisen toistensa pälle
        input_rect2_surface.fill((0, 0, 0)) #estää numeroiden päällekkäisyyden
        screen.blit(num_surface,input_rect2) #tällä pitäisi saada teksti näytölle
        pygame.draw.rect(screen,(3,0,0),input_rect2,2)
        pygame.display.flip() 
        print(self.num)


