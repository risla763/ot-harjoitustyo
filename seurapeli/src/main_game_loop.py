import sys
import pygame
from rects import GraphicGuess
from deck_of_cards import Deck
class Main:
    def __init__(self):
        pygame.init()
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
        self.font = pygame.font.SysFont(None, 77) #FONTTI ja fontin koko
        #kello
        deck = Deck()
        graphic = GraphicGuess()
        deck.draw(self.screen)
        graphic.draw_rect(self.screen)
        self.dealer_x = 100
        count = 2
        card = deck.deal()
        card.draw(self.screen, (100, 100))
        self.first_rank = card.get_rank()
        deck.count(self.screen,count, self.first_rank)
        #deck.count(self.screen,count,Deck().next_card)
        deck.next_card_dealer(self.screen,(1000,100)) #JAKAJAN EKA
        self.dealer_first_rank = Deck().next_card_dealer(self.screen,(1000,100))
        deck.count2(self.screen,count,self.dealer_first_rank)
        pygame.display.update()
        self.input_rect = pygame.Rect(100,890,493,60)
        self.try_again_rect = pygame.Rect(1000,890,493,60)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_rect.collidepoint(event.pos):
                        count += 1
                        if count == 3:
                            deck.next_card_dealer(self.screen,card_positions2)
                            deck.next_card(self.screen,card_positions)
                            deck.count(self.screen,count, self.first_rank)
                            deck.count2(self.screen,count,self.dealer_first_rank)
                        else:
                            deck.next_card(self.screen,card_positions)
                            deck.count(self.screen,count, self.first_rank)
                    if self.try_again_rect.collidepoint(event.pos):
                        count = 2
                        Main()
                x = count*100
                y = 100
                self.dealer_x = count*100+900
                b = 100
                card_positions = (x,y)
                card_positions2 = (self.dealer_x,b)
                #nämä voisi laitta draw_rect luokkaan
                self.user_text = "Jatketaanko peliä?"
                text_surface = self.font.render(self.user_text, True,(0,0,0))
                self.screen.blit(text_surface,self.input_rect) #tällä pitäisi saada teksti näytölle
                try_again_text = "Aloitetaanko alusta?"
                text_surface2 = self.font.render(try_again_text, True, (0,0,0))
                self.screen.blit(text_surface2,self.try_again_rect)
                pygame.display.flip() #tärkeä ja päivittää yhtä pientä
                pygame.display.update()
Main()
