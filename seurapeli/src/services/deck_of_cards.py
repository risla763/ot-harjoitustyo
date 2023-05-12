import random
import os
import pygame
from services.card_deck import Card
from services.score import Score
from services.flip_side import Flip
from services.ui.next_cards import draw_next


class Deck:
    """This class shuffles the card deck and
    has some logic in it how the counting and rounds work."""
    def __init__(self):
        """This is the constructor of the
        class and it has lists of colors and values of the cards.
        It also shuffles and makes the deck."""
        self.cards = []
        suits = ['spades', 'hearts', 'diamonds', 'clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'jack', 'queen', 'king', 'ace']
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank, self.cards)
                self.cards.append(card)  # tuple lista korteista
        random.shuffle(self.cards)  # sekoitetaan pakkaa
        self.fin, self.fin2 = 0, 0
        self.num, self.num2 = 0, 0
        self.first_rank = 0
        self.font = pygame.font.SysFont("Inter", 77)  # muokaa tätä draw_rect
        self.screen_width = 1800
        self.screen_height= 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.num_surface = 0
        self.input_rect = pygame.Rect(1390, 45, 70, 50)
        self.suit_imp = card.get_suit()
        png_directory = "PNG-cards-1.3"
        self.important_card = os.path.join(
            png_directory, f"{self.num2}_of_{self.suit_imp}.png")
        #self.important_image = pygame.image.load(self.important_card)
        self.input_rect_surface = 0
        self.score = Score(self.screen)

    def deal(self):
        """This method removes a card from the deck and returns it."""
        # poistaa ja palauttaa?
        return self.cards.pop()

    def next_card(self):
        """This method removes and returns a card from the deck too...
        also in this method card gets a variable where is its rank
        """
        card = self.cards.pop()
        self.num = card.get_rank()
        return card

    def next_card_dealer(self, screen, card_positions2, count_dealer):
        """This method deals the dealer a card.
        If the count_dealer is 0 (round starts) then that card will be face down.
        Args: 
            screen: displays the pygame screen
            card_positions2: tuple at which the card image is drawn
            count_dealer: a counter that keeps a sum of the dealer's card values
        Returns: the value of the card dealt
            """
        #every_card = len(self.cards)
        card = self.cards.pop()
        if count_dealer == 0:
            draw_next(screen, card_positions2,card)
            Flip(screen).draw(screen, (950, 60))
            self.num2 = card.get_rank()
            png_directory = "src/services/entities/PNG-cards-1.3"
            self.important_card = os.path.join(
                png_directory, f"{self.num2}_of_{self.suit_imp}.png")
            self.important_image = pygame.image.load(self.important_card)
            #print(self.important_card)
        else:
            draw_next(screen, card_positions2,card)
        self.num2 = card.get_rank()
        self.suit_imp = card.get_suit()
        return self.num2

    def count2(self, screen, count, dealer_first_rank):
        """This method keeps track of the sum of the values of the dealer's cards.
        Args: 
            screen: displays the pygame screen
            count: a counter that keeps a sum of the player's card values
            dealer_first_rank: the value of the dealer's first card"""
        if count <= 2:
            self.num2 = 0
            if dealer_first_rank == "king":
                final_num2 = int(13)
            elif dealer_first_rank == "queen":
                final_num2 = int(12)
            elif dealer_first_rank == "ace":
                final_num2 = int(14)
            elif dealer_first_rank == "jack":
                final_num2 = int(11)
            else:
                # tähän tarvitaan pinossa päällimmäisen kortin rankki dealer
                final_num2 = int(dealer_first_rank)
        else:
            final_num2 = self.fin2
        if self.num2 == "king":
            self.num2 = "13"
        elif self.num2 == "queen":
            self.num2 = "12"
        elif self.num2 == "jack":
            self.num2 = "11"
        elif self.num2 == "ace":
            self.num2 = "14"
        final_num2 += int(self.num2)
        font = pygame.font.SysFont(None, 77)
        self.num_surface = font.render(str(final_num2), True, (50, 40, 30))
        self.fin2 = final_num2
        # estää numeroiden menemisen toistensa pälle
        self.input_rect_surface = screen.subsurface(self.input_rect)
        self.screen = screen

    def count(self, screen, count, first_rank):
        """This methdon keeps track of the sum of the player's card values.
        Args:
            screen: displays the pygame screen
            count: a variable that keeps track of the number of card withdrawals
            first_rank: the value of the first card dealt to the player
            """
        if count <= 2:
            if first_rank == "king":
                final_num = int(13)
            elif first_rank == "queen":
                final_num = int(12)
            elif first_rank == "ace":
                final_num = int(14)
            elif first_rank == "jack":
                final_num = int(11)
            else:
                # tähän tarvitaan pinossa päällimmäisen kortin rankki
                final_num = int(first_rank)
        else:
            final_num = self.fin
        if self.num == "king":
            self.num = "13"
        elif self.num == "queen":
            self.num = "12"
        elif self.num == "jack":
            self.num = "11"
        elif self.num == "ace":
            self.num = "14"
        final_num += int(self.num)
        font = pygame.font.SysFont(None, 77)
        num_surface = font.render(str(final_num), True, (50, 40, 30))
        self.fin = final_num  # muuttuva numero
        input_rect2 = pygame.Rect(500, 45, 70, 50)
        # estää numeroiden menemisen toistensa pälle
        input_rect2_surface = screen.subsurface(input_rect2)
        # estää numeroiden päällekkäisyyden
        input_rect2_surface.fill((255, 255, 255))
        # tällä pitäisi saada teksti näytölle
        screen.blit(num_surface, input_rect2)
        pygame.draw.rect(screen, (3, 0, 0), input_rect2, 2)
        pygame.display.flip()
        #print("lollll", self.fin)
        # print(self.fin)
        if self.fin >= 22:
            self.first_rank = 0
            Deck.round_ends(self, screen)
            self.score.which_is_it(self.fin, self.fin2)
            return True

    def see_cards(self, screen):
        """This method takes to a different class and method
        where it is calculated who has won the round.
        Args:
            screen: displays the pygame screen"""
        value = self.score.which_is_it(self.fin, self.fin2)
        #tässä on vielä piirtämistä, jonka tulen siirtämään eri tiedostoon
        # tällä pitäisi saada teksti näytölle
        self.input_rect_surface.fill((255, 255, 255))  # valkoinen
        #screen.blit(game_over_surface, input_rect3)
        # screen.blit(self.important_image,(950,100))
        screen.blit(self.num_surface, self.input_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.input_rect, 2)  # (0,0,0)
        pygame.display.flip()
        # ei pysty enää nostaa uutta korttia
        return value
    
    def game_over_after_see_cards(self):
        return True

    def round_ends(self, screen):  #Tämän tulen siirtämään ui kansioon
        """This methdon draws "game over" on the screen
        Args:
            screen: displays the pygame screen"""
        self.enable = False
        # näytölle ilmestyy game over ja start again
        #self.font = pygame.font.SysFont(None, 77)
        game_over_surface = self.font.render(
            str("Game over"), True, (255, 255, 255))
        input_rect3 = pygame.Rect(800, 400, 70, 50)
        # tällä pitäisi saada teksti näytölle
        self.input_rect_surface.fill((255, 255, 255))
        screen.blit(game_over_surface, input_rect3)
        # screen.blit(self.important_image,(950,100)) #tässä sama tilanne kuin edellisessä
        screen.blit(self.num_surface, self.input_rect)
        pygame.draw.rect(screen, (0, 0, 0), self.input_rect, 2)  # (0,0,0)
        pygame.display.flip()
        return True
