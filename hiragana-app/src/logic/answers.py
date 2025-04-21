import pygame
import time
from ui.game_screen import GameScreen

class CheckAndReviev:

    def __init__(self, hiraganas):
        self.hiraganas_list = hiraganas

    def check_answer(self, hiragana_tuple, user_input, screen):
        syllable = str(hiragana_tuple[1])
        user_input = "{{'{}'}}".format(user_input)
        if syllable == user_input:
            answer = True
            GameScreen(screen).comment_if_correct(answer, syllable)
        else:
            answer = False
            syllable = syllable.replace('{','')
            syllable = syllable.replace('}','')
            GameScreen(screen).comment_if_correct(answer, syllable)

    #def scoreboard(self):
        #myös sellainen että kuinka monta kertaa kukin tavu mennyt oikein tai väärin
        #kun kirjautuu sisälle näkee..oman putken kuinka pitkään on saanut tavuja oikein peräkkäin
        #näkee mikä tavu heikoin
        #näkee mikä tavu paras
