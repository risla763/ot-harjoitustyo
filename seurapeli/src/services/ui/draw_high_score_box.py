from services.ui.draw_rect import Rect

def draw_new_deck_box(self,screen):
    self.hc_rect = Rect().make_changing_rect

        
    hc = self.hc_rect("New round starts",
            (255, 255, 255), (0, 0, 0), (255, 255, 255),(700, 15, 300, 50),screen)