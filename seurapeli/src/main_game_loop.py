import sys
import os
import pygame
from ui.rects import GraphicGuess
from deck_of_cards import Deck
from ui.draw_rect import Rect
from flip_side import Flip
from score import Score
from ui.draw_deck import draw_deck
from ui.next_cards import draw_next
class Main:
    def __init__(self):
        pygame.init()
        self.enable = True
        # pylint: disable=invalid-name
        self.screen_width = 1800
        self.screen_height= 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("blackjack harjoitin")
        #color2 = (0,181,20) #äglön vihreä
        self.color = (0, 139, 0)
        self.screen.fill(self.color)
        pygame.display.flip()
        #teksti
        self.font = pygame.font.SysFont('didot.ttc', 72) #FONTTI ja fontin koko
        deck = Deck()
        #deck.draw(self.screen)
        draw_deck(self,self.screen,deck)
        self.dealer_x = 100
        count = 2
        self.count_dealer = 0
        card = deck.deal()
        draw_next(self.screen, (100, 100),card)
        self.first_rank = card.get_rank()
        #deck.count(self.screen,count,Deck().next_card)
        deck.next_card_dealer(self.screen,(1000,100),self.count_dealer) #JAKAJAN EKA
        #
        self.dealer_first_rank = Deck().next_card_dealer(self.screen,(1000,100),self.count_dealer)
        self.dealer_first_suit = card.get_suit() #
        deck.count2(self.screen,count,self.dealer_first_rank)
        pygame.display.update()
        self.input_rect = pygame.Rect(100,890,493,60)
        self.try_again = Rect().make_changing_rect("Aloitetaanko alusta?", (100,149,237), (119, 5, 0), (255, 255, 255),(1200, 890, 400, 50),self.screen)
        self.try_again_rect = pygame.Rect(1200,890,400,50)
        self.game_continues = Rect().make_changing_rect("Jatketaanko peliä?",(100,149,237),(119,5,0),(255,255,255),(100,890,330,50),self.screen)
        self.end_round_rect = pygame.Rect(650,890,322,50)
        self.end_round = Rect().make_changing_rect("Katsotaanko kortit?", (100,149,237), (119, 5, 0), (255, 255, 255),(650, 890, 332, 50),self.screen)
        deck.count(self.screen,count, self.first_rank,self.enable)
        self.count_dealer += 1
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.enable == True:
                        if self.input_rect.collidepoint(event.pos):
                            count += 1
                            self.count_dealer += 1
                            if count == 3:
                                deck.next_card_dealer(self.screen,card_positions2,self.count_dealer)
                                next_card = deck.next_card()
                                draw_next(self.screen,card_positions,next_card)
                                deck.count(self.screen,count, self.first_rank,self.enable)
                                deck.count2(self.screen,count,self.dealer_first_rank)
                            else:
                                next_card = deck.next_card()
                                draw_next(self.screen,card_positions,next_card)
                                deck.count(self.screen,count, self.first_rank,self.enable)
                    if self.try_again_rect.collidepoint(event.pos):
                        count = 2
                        self.enable = False
                        Main()
                    if self.end_round_rect.collidepoint(event.pos):
                        #print("moi")
                        deck.see_cards(self.screen)
                        self.enable = False
            
                x = count*100
                y = 100
                self.dealer_x = count*100+900
                b = 100
                card_positions = (x,y)
                card_positions2 = (self.dealer_x,b)
                pygame.display.flip() #tärkeä ja päivittää yhtä pientä
                pygame.display.update()
                #TÄNNE TULEE 0-0 SCORE JUTTU
Main()
