import pygame
import random
import os
from PIL import Image
import time
#from main import Main
from pygame.locals import *
from input import GraphicGuess
#from card import Card
#from main import Deck #card_deck on oikea nimi
from card_deck import Card
from score import Score
from changes_card_deck import Deck



class Main:
    def __init__(self):

        print("HALOO")
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
    
    #def start_game(self): 

# Create a deck of cards
        deck = Deck()
        graphic = GraphicGuess()

# Draw the deck of cards PIIRTÄÄ KORTTIPAKAN
        deck.draw(screen, (10, 10))
    #ekan rank jo eli first_rank = card.get_rank 

        graphic.draw_rect(screen)

    #graphic.draw_rect2(screen)
    
    #graphic.draw_rect3(screen)


        a = 100
        i = 51
        count = 2
# Deal a card and draw it on the screen #yksittäinen kortti
    #print("moi")


        card = deck.deal()
        #deck.next_card(screen,(100,100))
        card.draw(screen, (100, 100)) #piirrä tämä siihen kohtaan TÄMÄ KOHTA EITYISEN TÄRKEÄ
        self.first_rank = card.get_rank() #EKAN RANKKI EI JAKAJA
        deck.count(screen,count, self.first_rank) #laskuri suoraan ruudussa
        



        #deck.count(screen,count,Deck().next_card)
        deck.next_card_dealer(screen,(1000,100)) #JAKAJAN EKA
        self.dealer_first_rank = Deck().next_card_dealer(screen,(1000,100))
        deck.count2(screen,count,self.dealer_first_rank)

    # Update the display
        pygame.display.update()
        input_rect = pygame.Rect(100,890,493,60)
        try_again_rect = pygame.Rect(1000,890,493,60)
        
        new_try_count = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                        #active = True
            
                    if input_rect.collidepoint(event.pos):

                        count += 1
                        
                        if count == 3:
                                deck.next_card_dealer(screen,card_positions2)
                                deck.next_card(screen,card_positions)
                                deck.count(screen,count, self.first_rank)
                                deck.count2(screen,count,self.dealer_first_rank)
                        else:
                            deck.next_card(screen,card_positions)
                            deck.count(screen,count, self.first_rank)
                    
                    if try_again_rect.collidepoint(event.pos):
                        count = 2
                        fin = 0
                        fin2 = 0
                        Main() #tässä vierailee countissa
                        print("lol")
                        #first_rank2 = NewTry().first_rank #näiden takia kortti vilahti
                        #dealer_first_rank2= NewTry().dealer_first_rank

    #Miksi count metodi ei nollaannu?

    
                    
                x = count*100
                y = 100
                a = count*100+900
                b = 100
                card_positions = (x,y)  
                card_positions2 = (a,b)
                user_text = "Jatketaanko peliä?"
                text_surface = font.render(user_text, True,(0,0,0))


            #laskuri, joka laskee korttien summan
            #num = card.get_rank siirrä next_card metodiin
            #text_surface_calculator = font.render(str(num),True, (0,0,0))
            #tekstin paikka
            
                screen.blit(text_surface,input_rect) #tällä pitäisi saada teksti näytölle

                try_again_text = "Aloitetaanko alusta?"
                text_surface2 = font.render(try_again_text, True, (0,0,0))
                screen.blit(text_surface2,try_again_rect)
                #pygame.draw.rect(screen,(3,0,0),input_rect2,2)
                #pygame.draw.rect(screen,(255,255,255),try_again_rect)
                pygame.display.flip() #tärkeä ja päivittää yhtä pientä
            #rectangle = pygame.Rect(0,0,50,50)
            #pygame.draw.rect(screen, color, rectangle)
            #rectangle.fill(color)
                #elapsed_time = int(time.time() - start_time)


        # Render the timer display
            #timer_display = font.render(f"Time: {elapsed_time}", True, (0, 0, 0))
            #screen.blit(timer_display, (10, 10))

                pygame.display.update()

Main()