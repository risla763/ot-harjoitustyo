import pygame
from objects.button_rect import ButtonRect
from logic.hiragana_pictures import HiraganaPictureLogic

class GameScreen:

    def __init__(self):
        self. pink = (255, 182, 193)
        self.white = (255, 255, 255)

    def game_screen(self, screen):
        screen.fill((255, 204, 229))  
        font = pygame.font.SysFont(None, 50)
        text_surface = font.render("Game comes here", True, (173, 216, 230))
        screen.blit(text_surface, (200, 200))
        HiraganaPictureLogic(screen)
        pygame.display.flip()

    def make_input_field(self, position, screen):
        self.start_game_button = ButtonRect().make_rect("",
            self.pink,
            self.white,
            position,
            screen
        )
        return self.start_game_button
