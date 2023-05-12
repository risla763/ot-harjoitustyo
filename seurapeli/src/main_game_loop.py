import sys
import pygame
from services.deck_of_cards import Deck
from services.ui.draw_rect import Rect
from services.ui.draw_deck import draw_deck
from services.ui.next_cards import draw_next
from services.score import Score
class Main:
    """This class defines the game screen values and other 
    values used in the game like point counters values. 
    This class also calls other classes in the game
        """
    def __init__(self):
        """Class constructor that creates a new game.
        """
        pygame.init()
        self.value = 0,0
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
        self.deck = Deck()
        #self.deck.draw(self.screen)
        draw_deck(self,self.screen,self.deck)
        self.dealer_x = 100
        count = 2
        self.count_dealer = 0
        card = self.deck.deal()
        draw_next(self.screen, (100, 100),card)
        self.first_rank = card.get_rank()
        self.restart(self.screen)

    def restart(self,screen):
        self.deck.fin, self.deck.fin2 = 0, 0
        self.deck.num, self.deck.num2 = 0, 0
        self.deck.first_rank = 0
        self.deck.num_surface = 0
        print(self.value)
        self.enable = True
        #self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(self.color)
        pygame.display.flip()
        #teksti
        self.font = pygame.font.SysFont('didot.ttc', 72) #FONTTI ja fontin koko
        #self.deck.draw(self.screen)
        draw_deck(self,self.screen,self.deck)
        self.dealer_x = 100
        count = 2
        self.count_dealer = 0
        card = self.deck.deal()
        draw_next(self.screen, (100, 100),card)
        self.first_rank = card.get_rank()
        #self.deck.count(self.screen,count,Deck().next_card)
        self.deck.next_card_dealer(self.screen,(1000,100),self.count_dealer) #JAKAJAN EKA
        #
        #
        self.dealer_first_rank = self.deck.next_card_dealer(self.screen,(1000,100),self.count_dealer)
        self.dealer_first_suit = card.get_suit() #
        self.deck.count2(self.screen,count,self.dealer_first_rank)
        pygame.display.update()
        self.input_rect = pygame.Rect(100,890,493,60)
        self.try_again = Rect().make_changing_rect("Aloitetaanko alusta?",
                                                   (100,149,237), (119, 5, 0), (255, 255, 255),
                                                   (1200, 890, 400, 50),self.screen)
        self.try_again_rect = pygame.Rect(1200,890,400,50)
        self.game_continues = Rect().make_changing_rect("Jatketaanko peliä?",
                                                        (100,149,237),(119,5,0),
                                                        (255,255,255),(100,890,330,50),self.screen)
        self.end_round_rect = pygame.Rect(650,890,322,50)
        self.end_round = Rect().make_changing_rect("Katsotaanko kortit?",
                                                   (100,149,237), (119, 5, 0),
                                                   (255, 255, 255),(650, 890, 332, 50),self.screen)
        self.deck.count(self.screen,count, self.first_rank)
        self.count_dealer += 1
        self.game_loop()

    def game_loop(self):
        game_over = False
        count = 2
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.enable == True:
                        if not game_over and self.input_rect.collidepoint(event.pos):
                            count += 1
                            self.count_dealer += 1
                            if count == 3:
                                self.deck.next_card_dealer(self.screen,card_positions2,self.count_dealer)
                                next_card = self.deck.next_card()
                                draw_next(self.screen,card_positions,next_card)
                                game_over = self.deck.count(self.screen,count, self.first_rank)
                                self.deck.count2(self.screen,count,self.dealer_first_rank)
                            else:
                                next_card = self.deck.next_card()
                                draw_next(self.screen,card_positions,next_card)
                                game_over= self.deck.count(self.screen,count, self.first_rank)
                                print(game_over)
                    if self.try_again_rect.collidepoint(event.pos):
                        count = 2
                        self.enable = False
                        #Main()
                        self.restart(self.screen)
                    if self.end_round_rect.collidepoint(event.pos): #katsotaanko kortit
                        #print("moi")
                        if game_over == True:
                            continue
                        else:
                            self.value = self.deck.see_cards(self.screen)
                            game_over = self.deck.game_over_after_see_cards()
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
main = Main()
main.restart
