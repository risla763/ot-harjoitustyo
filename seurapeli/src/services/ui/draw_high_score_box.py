from services.ui.draw_rect import Rect
"""This method draw the box on screen which contains the high score."""
def draw_new_deck_box(self,screen):
    self.hc_rect = Rect().make_changing_rect

        
    hc = self.hc_rect("Deck empty, new round starts",
            (255, 255, 255), (0, 0, 0), (255, 255, 255),(570, 15, 500, 50),screen)