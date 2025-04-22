import pygame
from objects.rect import ButtonRect
from ui.button_ui import Buttons

class MenuScreen:
    """Tämä luokka käsittelee menu näytöllä olevaa ui:ta.
    """

    def __init__(self):
        pygame.init() #onko turha

    #chatgpt auttoi tämän metodin luomisessa
    def game_menu_screen(self, screen):
        """Tämö metodi värittää näytön liilaksi ja tekee start game button ja scoreboard button.
        Args:
            screen: näyttö, jolle menu screen piirtyy.
        """
        screen.fill("purple")
        global start_game_button
        start_game_button = Buttons(screen).make_rect("start game",(200, 200, 190, 40))
        global scoreboard_button 
        scoreboard_button = Buttons(screen).make_rect("score board",(400, 200, 190, 40))

#kuva taulukosta missä kaikki hiraganat ja tavut niille