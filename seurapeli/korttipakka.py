import pygame
import random
import os
from PIL import Image
import time
#from main import Main
from input import GraphicGuess

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
                card = Card(suit, rank, self.cards) #yksittäinen kortti (TUPLE) tässä hypätään ylempään luokkaan
                self.cards.append(card) #tuple lista korteista
        random.shuffle(self.cards) #sekoitetaan pakkaa

    def draw(self, surface, pos): #piirtää koko pakan
        list_of_three_cards = []
        a = 650
        #a = 100
        i = 0
        for n,card in enumerate(self.cards): #i on indeksi (kuinka mones) mutta loopissa toimitaan tuplejen kanssa #i, 
            if i >= 50:
                card.draw(surface, (a,100))
                #a = 650
                a += 550
                list_of_three_cards.append(card)
            else:
                card.draw(surface, (100,100)) #tämä pistää kortin kuvan näytölle (x,y) #(pos[0] + i * 20, pos[1]) koritit levitettyinä #piirrä kolme viimeistä levitettyinä
                #tämä pistää kortin kuvan näytölle (x,y) #(pos[0] + i * 20, pos[1]) koritit levitettyinä #piirrä kolme viimeistä levitettyinä
                if i == 50:
                    list_of_three_cards.append(card)
            i += 1
        return list_of_three_cards
    def deal(self):
        return self.cards.pop() #poistaa kierroksella jaetun kortin (tähän pitää myös saada aikaiseksi se, että niitä on kolme)

class Main:
# Initialize Pygame
    pygame.init()

# Set up the display
    screen_width = 1800
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("F the dealer")
    color2 = (0,181,20) #äglön vihreä
    color = (0, 139, 0)
    screen.fill(color)
    pygame.display.flip()
    #teksti
    font = pygame.font.Font(None, 36)
    user_text = ''
    #kello
    start_time = time.time()


#teksti

    




# Create a deck of cards
    deck = Deck()
    graphic = GraphicGuess()

# Draw the deck of cards PIIRTÄÄ KORTTIPAKAN
    deck.draw(screen, (10, 10))

    graphic.draw_rect(screen)

    graphic.draw_rect2(screen)
    
    graphic.draw_rect3(screen)



# Deal a card and draw it on the screen #yksittäinen kortti
    card = deck.deal()
    #card.draw(screen, (100, 100)) #piirrä tämä siihen kohtaan

# Update the display
    pygame.display.update()
    input_rect = pygame.Rect(200,200,14,32)
# Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            #teksti boxeihin
            elif event.type == pygame.K_LEFT:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode 

        text_surface = font.render(user_text, True,(0,0,0))
        screen.blit(text_surface,input_rect)
        pygame.draw.rect(screen,(0,0,0),input_rect,2)

        #rectangle = pygame.Rect(0,0,50,50)
        #pygame.draw.rect(screen, color, rectangle)
        #rectangle.fill(color)
        elapsed_time = int(time.time() - start_time)


    # Render the timer display
        timer_display = font.render(f"Time: {elapsed_time}", True, (255, 255, 255))
        screen.blit(timer_display, (10, 10))

        pygame.display.update()