import pygame


class GraphicGuess:
    def __init__(self):
        # pylint: disable=E1101
        pygame.init()

    @staticmethod
    def draw_rect(screen):
        # # set the rectangle dimensions
        rect_width = 493
        rect_height = 60

#         screen_width = 1800
#         screen_height = 1000
#         screen = pygame.display.set_mode((screen_width, screen_height))

# calculate the rectangle position
        rect_x = 100
        rect_y = 1000 - 110

    #   teksti


# draw the rectangle
        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, (119, 5, 0), rect)
        pygame.display.flip()
    @staticmethod
    def draw_rect2(screen):
        # # set the rectangle dimensions
        rect_width = 493
        rect_height = 60

#         screen_width = 1800
#         screen_height = 1000
#         screen = pygame.display.set_mode((screen_width, screen_height))

# calculate the rectangle position
        rect_x = 653
        rect_y = 1000 - 110

# draw the rectangle
        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, (119, 5, 0), rect)
        pygame.display.flip()
    @staticmethod
    def draw_rect3(screen):
        # # set the rectangle dimensions
        rect_width = 493
        rect_height = 60

#         screen_width = 1800
#         screen_height = 1000
#         screen = pygame.display.set_mode((screen_width, screen_height))

# calculate the rectangle position
        rect_x = 1210
        rect_y = 1000 - 110

# draw the rectangle
        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, (119, 5, 0), rect)
        pygame.display.flip()

    #def text1(self):
        #font = pygame.font.SysFont("Arial", 24)
        #text = input("")
