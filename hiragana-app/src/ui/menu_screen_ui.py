import pygame
from objects.buttons import Button
from ui.make_rect import Rect

class MenuScreen:

    def __init__(self):
        pygame.init()

    #chatgpt auttoi tämän metodin luomisessa
    def game_menu_screen(self, screen):
        screen.fill("purple")
        global start_game_button
        start_game_button = Rect(screen).make_rect("start game",(200, 200, 190, 40))
        global scoreboard_button 
        scoreboard_button = Rect(screen).make_rect("score board",(400, 200, 190, 40))