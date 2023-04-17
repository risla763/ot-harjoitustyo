import pygame
import random
import os
from PIL import Image
import time
from card_deck import Card
from draw_rect import Rect

class Score:
    def __init__(self):
        self.player_score = 0
        self.dealer_score = 0
        self.j = 0
        self.p = 0

    def which_is_it(self,count,fin,fin2,screen):
        if abs(fin-21) < abs(fin2-21):
            print("eka laskuri")
            if fin > 21 and fin2<= 21:
                print("jakaja on voittanut")
                self.j += 1
                Rect().make_changing_rect(((self.p)-(self.j)),(255,255,255),(0,0,0),(255,255,255),screen)
            #score box
            else:
                print("Pelaaja on voittanut",fin)
                self.p += 1
                Rect().make_changing_rect(((self.p)-(self.j)),(255,255,255),(0,0,0),(255,255,255),screen)

        elif abs(fin2-21) < abs(fin-21):
            if fin2 > 21 and fin <= 21:
                print("Pelaaja on voittanut")
                self.p += 1
                Rect().make_changing_rect(((self.p)-(self.j)),(255,255,255),(0,0,0),(255,255,255),screen)
            #svorebox
            else:
                print("tässä jakajan",abs(fin2-21))
                print("Tässä pelaajan", abs(fin-21))
                print("Jakaja on voittanut",fin2, "Pelaaja:",fin)
                self.j += 1
                Rect().make_changing_rect(((self.p)-(self.j)),(255,255,255),(0,0,0),(255,255,255),screen)
        elif fin2 == fin:
            print(fin)
            print(fin2)



    

