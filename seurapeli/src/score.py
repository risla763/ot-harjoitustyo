from draw_rect import Rect

class Score:
    def __init__(self):
        self.dealer, self.player = 0, 0
    def which_is_it(self,fin, fin2, screen):
        if abs(fin-21) < abs(fin2-21):
            if fin > 21 > fin2:
                self.dealer += 1
                Rect().make_changing_rect(((self.player)-(self.dealer)),
                                          (255, 255, 255), (0, 0, 0), (255, 255, 255), screen)
            else:
                self.player += 1
                Rect().make_changing_rect(((self.player)-(self.dealer)),
                                          (255, 255, 255), (0, 0, 0), (255, 255, 255), screen)

        elif abs(fin2-21) < abs(fin-21):
            if fin2 > 21 > fin:
                self.player += 1
                Rect().make_changing_rect(((self.player)-(self.dealer)),
                                          (255, 255, 255), (0, 0, 0), (255, 255, 255), screen)
            else:
                self.dealer += 1
                Rect().make_changing_rect(((self.player)-(self.dealer)),
                                          (255, 255, 255), (0, 0, 0), (255, 255, 255), screen)
        elif fin2 == fin:
            print(fin)
            print(fin2)
