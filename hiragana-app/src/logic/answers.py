import pygame
from ui.game_screen import GameScreen

class CheckAndReviev:
    """Luokka, jonka tarkoituksena on tarkistaa vastaako 
    käyttäjän antama tavu hiraganaa, joka näytöllä on.
    
    Attributes:
        hiraganas_list: lista, jossa on generoitu lista tupleja, joissa
        ensimmäinen elementti on kuva hiraganasta ja toinen elementti on sit vastaava
        tavu."""

    def __init__(self, hiraganas):
        """Konstruktori, joka perii listan hiraganoja.
        Args:
            hiraganas: Lista täynnä hiraganoja ja niitä vastaavia tavuja.
            score: Pitää kirjaa kuinka monta hiraganaa käyttäjä 
            on tällä pelikerralla saanut oikein"""
        self.hiraganas_list = hiraganas

    def check_answer(self, hiragana_tuple, user_input, screen, score):
        """Tarkistaa onko käyttäjän syöttämä tavu sama 
        kuin näytöllä olevaa hiraganaa vastaava tavu
        
        Args: 
            hiragana_tuple: on tuple, jossa näytöllä näkyvä hiraganaa vastaava kuva, sekä
            sitä vastaava tavu
            user_input: on käyttäjän syöttämä input eli tavu
            screen: on ohjelman näyttö
        Returns: 
            answer: True, jos käyttäjän user_input vastaa tuplen sisällä olevaa tavua ja
            muuten False"""
        syllable = str(hiragana_tuple[1])
        user_input = "{{'{}'}}".format(user_input)
        if syllable == user_input:
            answer = True
            self.comment_if_correct(answer, syllable, screen)
            score += 1
            return answer, score
        else:
            answer = False
            syllable = syllable.replace('{','')
            syllable = syllable.replace('}','')
            self.comment_if_correct(answer, syllable, screen)
            return answer, score


    def comment_if_correct(self, answer, syllable, screen):
        """Näytölle ilmestyy kommentti vähäksi aikaa, jossa lukee onko käyttäjän antama
        vastaus on oikein vai väärin
        
        Args: 
            amswer: True, jos käyttäjän input oli oikein ja muussa tapauksessa False
            syllable: oikea vastaus (tavu), joka on saatu tuplesta
            screen: pelin näyttö """
        i = 0
        if answer == True:
            while i < 60:
                ticks=pygame.time.get_ticks()
                GameScreen(screen).comment_ui_right(answer, syllable)
                i = i+1
        else:
            while i < 200:
                ticks=pygame.time.get_ticks()
                GameScreen(screen).comment_ui_wrong(answer, syllable)
                i = i+1
        GameScreen(screen).clear_comment_field()


    #def scoreboard(self):
        #myös sellainen että kuinka monta kertaa kukin tavu mennyt oikein tai väärin
        #kun kirjautuu sisälle näkee..oman putken kuinka pitkään on saanut tavuja oikein peräkkäin
        #näkee mikä tavu heikoin
        #näkee mikä tavu paras
