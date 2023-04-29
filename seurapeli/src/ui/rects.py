import pygame

"""This class draws dark red rectangles on the screen that can be used below the texts."""
class GraphicGuess:
    def __init__(self):
        # pylint: disable=E1101
        pygame.init()

    @staticmethod
    def draw_rect(screen):
        rect_width = 493
        rect_height = 60

        rect_x = 100
        rect_y = 1000 - 110

        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, (119, 5, 0), rect)
        pygame.display.flip()
    @staticmethod
    def draw_rect2(screen):
        rect_width = 493
        rect_height = 60

        rect_x = 653
        rect_y = 1000 - 110
        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, (119, 5, 0), rect)
        pygame.display.flip()
    @staticmethod
    def draw_rect3(screen):
        rect_width = 493
        rect_height = 60
        rect_x = 1210
        rect_y = 1000 - 110

        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, (119, 5, 0), rect)
        pygame.display.flip()
