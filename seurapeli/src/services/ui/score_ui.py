
from services.ui.draw_rect import Rect



def draw_score(self,player,dealer):
        """This method draws the score on the screen.
        Args:
            self.player_rect: a rect that contains the players score
            self.dealer_rect: a rect that contains the dealers score"""
        self.dealer_rect = Rect().make_changing_rect
        self.player_rect = Rect().make_changing_rect2
        
        play = self.player_rect(self.player,
                         (255, 255, 255), (0, 0, 0), (255, 255, 255),(1090, 15, 50, 50),self.screen)
        #tähän viiva
        dea = self.dealer_rect(self.dealer,
                         (255, 255, 255), (0, 0, 0), (255, 255, 255),(1140,15,50,50),self.screen)

        return player



