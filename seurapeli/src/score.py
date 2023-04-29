from ui.draw_rect import Rect
import pygame.font
import pygame

class Score:
    def __init__(self,screen):
        self.font = pygame.font.Font(None, 36)
        self.dealer, self.player = 0, 0
        self.dealer_rect = Rect().make_changing_rect
        self.player_rect = Rect().make_changing_rect2
        self.screen = screen
    def which_is_it(self,fin, fin2, screen):
        if abs(fin-21) < abs(fin2-21):
            if fin > 21 > fin2:
                self.dealer += 1

            else:
                self.player += 1


        elif abs(fin2-21) < abs(fin-21):
            if fin2 > 21 > fin:
                self.player += 1

            else:
                self.dealer += 1

        elif fin2 == fin:
            print(fin)
            print(fin2)



        self.player_rect(self.player, (255, 255, 255), (0, 0, 0), (255, 255, 255),(1070, 15, 50, 50),self.screen)
        #tähän viiva
        self.dealer_rect(self.dealer, (255, 255, 255), (0, 0, 0), (255, 255, 255),(1120,15,50,50),self.screen)



