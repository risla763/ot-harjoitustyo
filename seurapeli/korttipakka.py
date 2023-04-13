import pygame
import random
import os
from PIL import Image
import time
#from main import Main
from pygame.locals import *
from input import GraphicGuess
#from main import Deck #card_deck on oikea nimi







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


        
    def count(self, screen,count,first_rank):
        if count <= 3:
            if first_rank == "king":
                final_num = int(13)
            elif first_rank == "queen":
                final_num = int(12)
            elif first_rank == "ace":
                final_num = int(14)
            elif first_rank == "jack":
                final_num = int(11)
            else:
                final_num = int(first_rank) #tähän tarvitaan pinossa päällimmäisen kortin rankki
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
        num_surface = font.render(str(final_num),True,(50,40,30))
        self.fin = final_num
        input_rect2 = pygame.Rect(500,45,70,50)
        input_rect2_surface = screen.subsurface(input_rect2) #estää numeroiden menemisen toistensa pälle
        input_rect2_surface.fill((255, 255, 255)) #estää numeroiden päällekkäisyyden
        screen.blit(num_surface,input_rect2) #tällä pitäisi saada teksti näytölle
        pygame.draw.rect(screen,(3,0,0),input_rect2,2)
        pygame.display.flip() 
        print(self.fin)
        self.screen = screen
        if self.fin >= 21:
            Deck.game_ends(screen)

    def game_ends(screen):
            #näytölle ilmestyy game over ja start again
            font = pygame.font.SysFont(None, 77) 
            game_over_surface = font.render(str("Game over"),True,(255,255,255))
            input_rect3 = pygame.Rect(800,45,70,50)
            screen.blit(game_over_surface,input_rect3) #tällä pitäisi saada teksti näytölle
            #pygame.draw.rect(screen,(3,0,0),input_rect3,2)
            pygame.display.flip() 
            
    #def point_counter(self)
        #laskee kuinka plajon pisteitä eli onko voiittanut jakajan vai ei?
        





class Main:
# Initialize Pygame
    pygame.init()

# Set up the display
    screen_width = 1800
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("blackjack harjoitin")
    color2 = (0,181,20) #äglön vihreä
    color = (0, 139, 0)

    screen.fill(color)
    pygame.display.flip()
    #teksti
    font = pygame.font.SysFont(None, 77) #FONTTI ja fontin koko
    user_text = '' #käyttäjän inputtaama teksti
    #kello
    start_time = time.time()
    #text_21 = font
    

#teksti


# Create a deck of cards
    deck = Deck()
    graphic = GraphicGuess()

# Draw the deck of cards PIIRTÄÄ KORTTIPAKAN
    deck.draw(screen, (10, 10))

    graphic.draw_rect(screen)

    #graphic.draw_rect2(screen)
    
    #graphic.draw_rect3(screen)



# Deal a card and draw it on the screen #yksittäinen kortti
    card = deck.deal()
    card.draw(screen, (100, 100)) #piirrä tämä siihen kohtaan TÄMÄ KOHTA EITYISEN TÄRKEÄ
    first_rank = card.get_rank()
    print(first_rank)
# Update the display
    pygame.display.update()
    input_rect = pygame.Rect(100,890,493,60)
    #input_rect = graphic.draw_rect(screen)
# Game loop
    a = 100
    i = 51
    count = 2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                #active = True
           
                if input_rect.collidepoint(event.pos):
                    #card_positions = [(200,100),(300,100),(400,100)]
                    #deck.deal()
                    #i = 200
                    count += 1
                    deck.next_card(screen,card_positions)
                    deck.count(screen,count, first_rank)
                

   
                    
                    
                #if active:
                    #nostaa uuden kortin
                    #if event.key == pygame.K_RETURN:
                        #print(user_text)
                        #text = ''
                        #active = False
                    #elif event.key == pygame.K_BACKSPACE:
                        #user_text = user_text.rstrip(user_text[-1]) #teksti vielä pitää poistaa näytöltä
                        #screen.fill(pygame.Color(119, 5, 0),(100,890,493,60)) #jotenkin toimii...jos kaksi vikaa kirjainta on samat niin poistaa molemmatu
                    #else:
                        #user_text += event.unicode 
        x = count*100
        y = 100
        card_positions = (x,y)  
        user_text = "Jatketaanko peliä?"
        text_surface = font.render(user_text, True,(0,0,0))
        #laskuri, joka laskee korttien summan
        #num = card.get_rank siirrä next_card metodiin
        #text_surface_calculator = font.render(str(num),True, (0,0,0))
        #tekstin paikka
        screen.blit(text_surface,input_rect) #tällä pitäisi saada teksti näytölle
        pygame.draw.rect(screen,(0,0,0),input_rect,2)
        pygame.display.flip() #tärkeä ja päivittää yhtä pientä
        #rectangle = pygame.Rect(0,0,50,50)
        #pygame.draw.rect(screen, color, rectangle)
        #rectangle.fill(color)
        elapsed_time = int(time.time() - start_time)


    # Render the timer display
        #timer_display = font.render(f"Time: {elapsed_time}", True, (0, 0, 0))
        #screen.blit(timer_display, (10, 10))

        pygame.display.update()