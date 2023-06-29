import pygame.font
import pygame
from services.ui.draw_rect import Rect
from services.ui.score_ui import draw_score
from services.write_to_file import write_to_file
from services.ui.tie_ui import draw_tie

class Score:
    """This class keeps track of who has won more rounds, the dealer or the player
    Attributes: 
        screen: displays the pygame screen"""
    def __init__(self,screen):
        """This is the constructor of the class and it sets the sarting values to zero
        Args: 
            screen: displays the pygame screen"""
        #self.font = pygame.font.Font(None, 36)
        self.dealer, self.player = 0, 0
        self.dealer_rect = Rect().make_changing_rect
        self.player_rect = Rect().make_changing_rect2
        self.screen_width = 1800
        self.screen_height= 1000
        #self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen = screen
        self.counter = 0
        self.switch = False
    def which_is_it(self,fin, fin2):
        """This method compares the sum of the players' cards in the round and calculates
        who wins that round
        Args:
            fin: the sum of the cards drawn by the player
            fin2: the sum of the cards drawn by the dealer
        Draws who won on the screen."""
        if self.switch != True:
            if abs(fin-21) < abs(fin2-21):
                if fin > 21 > fin2:
                    self.dealer += 1
                    draw_score(self,self.player,self.dealer)
                else:
                    self.player += 1
                    draw_score(self,self.player,self.dealer)
            elif abs(fin2-21) < abs(fin-21):
                if fin2 > 21 > fin:
                    self.player += 1
                    draw_score(self,self.player,self.dealer)
                else:
                    self.dealer += 1
                    draw_score(self,self.player,self.dealer)
            elif abs(fin2-21) == abs(fin-21):
                draw_tie(self)
            self.saved_value = self.player
            return self.player,self.dealer
        else:
            self.saved_value = self.player
            self.switch = False
            return self.player,self.dealer
    
    def player_high_score(self):
        """This method fetches the value of self.player which is the score what the player gets every round total."""
        self.switch = True
        player_value, _ = self.which_is_it(self.player, 0)
        return self.saved_value

