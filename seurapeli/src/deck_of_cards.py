import random
import time
# from main import Main
import pygame
# from card import Card
# from main import Deck #card_deck on oikea nimi
from card_deck import Card
from score import Score
class Deck:  # korttipakka
    def __init__(self):
        self.cards = []
        suits = ['spades', 'hearts', 'diamonds', 'clubs']
        ranks = ['2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'jack', 'queen', 'king', 'ace']
        for suit in suits:  # värit
            for rank in ranks:  # arvot
                # yksittäinen kortti (TUPLE) tässä hypätään ylempään luokkaan
                card = Card(suit, rank, self.cards)
                self.cards.append(card)  # tuple lista korteista
        random.shuffle(self.cards)  # sekoitetaan pakkaa
        #self.list_of_three_cards = []
        self.fin, self.fin2 =0,0
        self.num, self.num2 = 0,0
        self.first_rank = 0
        self.font = pygame.font.SysFont(None, 77) #muokaa tätä draw_rect
        self.screen = 0

    def draw(self, surface):  # piirtää koko pakan
        for card in self.cards:
            # tämä pistää kortin kuvan näytölle (x,y) #(pos[0] + i * 20, pos[1])
            card.draw(surface, (100, 100))
            # tämä pistää kortin kuvan näytölle (x,y) #(pos[0] + i * 20, pos[1])
            # if i == 50:
            #self.list_of_three_cards.append(card)
            # i += 1
        return print(enumerate(self.cards))

    def deal(self):
        # poistaa ja palauttaa?
        return self.cards.pop()

    def next_card(self, screen, card_positions):
        #every_card = len(self.cards)
        card = self.cards.pop()
        # menee Card luokan draw metodiin
        card.draw(screen, card_positions)
        # kutsutaan samaa korttia uudestaan, että saadaan rank
        # NUMERO LASKURI TÄHÄN, KOSKA TÄMÄ METODI PERII RUUDUN
        self.num = card.get_rank()
        # self.old_rank = card.get_rank()

    def next_card_dealer(self, screen, card_positions2):
        #every_card = len(self.cards)

        card = self.cards.pop()
        card.draw(screen, card_positions2)
        self.num2 = card.get_rank()
        return self.num2

    def count2(self, screen, count, dealer_first_rank):
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
        num_surface = font.render(str(final_num2), True, (50, 40, 30))
        self.fin2 = final_num2
        input_rect22 = pygame.Rect(1390, 45, 70, 50)
        # estää numeroiden menemisen toistensa pälle
        input_rect22_surface = screen.subsurface(input_rect22)
        # estää numeroiden päällekkäisyyden
        input_rect22_surface.fill((255, 255, 255))
        # tällä pitäisi saada teksti näytölle
        screen.blit(num_surface, input_rect22)
        pygame.draw.rect(screen, (0, 0, 0), input_rect22, 2)  # (0,0,0)
        pygame.display.flip()
        print(self.fin2)
        self.screen = screen

    def count(self, screen, count, first_rank):
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
        print("lollll", self.fin)
        # print(self.fin)
        if self.fin >= 22:
            self.first_rank = 0
            Deck.round_ends(self, screen)
            Score().which_is_it(self.fin, self.fin2, self.screen)

    def round_ends(self, screen):  # GAME OVER
        # näytölle ilmestyy game over ja start again
        #self.font = pygame.font.SysFont(None, 77)
        game_over_surface = self.font.render(
            str("Game over"), True, (255, 255, 255))
        input_rect3 = pygame.Rect(800, 45, 70, 50)
        # tällä pitäisi saada teksti näytölle
        screen.blit(game_over_surface, input_rect3)
        pygame.display.flip()
