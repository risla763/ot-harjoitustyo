import pygame
from objects.rect import ButtonRect
from ui.button_ui import Buttons

class MenuScreen:

    def __init__(self):
        pygame.init() #onko turha

    #chatgpt auttoi tämän metodin luomisessa
    def game_menu_screen(self, screen):
        screen.fill("purple")
        global start_game_button
        start_game_button = Buttons(screen).make_rect("start game",(200, 200, 190, 40))
        global scoreboard_button 
        scoreboard_button = Buttons(screen).make_rect("score board",(400, 200, 190, 40))

#kuva taulukosta missä kaikki hiraganat ja tavut niille