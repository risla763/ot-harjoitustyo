import pygame
"""This class draws rectangles with text."""
class Rect:
    #@staticmethod

    def make_changing_rect(self,text, text_color, surface_color, frames_color,rect_position, screen):
        font = pygame.font.SysFont(None, 50)
        surface = font.render(str(text), True, text_color)

        rect = pygame.Rect(rect_position)

        rect_surface = screen.subsurface(rect)
        rect_surface.fill(surface_color)
        screen.blit(surface, rect)
        pygame.draw.rect(screen, frames_color, rect,
                         2)
        pygame.display.flip()

    def make_changing_rect2(self,text, text_color, surface_color, frames_color,rect_position,screen):
            font = pygame.font.SysFont(None, 50)
            surface = font.render(str(text), True, text_color)

            rect = pygame.Rect(rect_position)

            rect_surface = screen.subsurface(rect)
            rect_surface.fill(surface_color)
            screen.blit(surface, rect)
            pygame.draw.rect(screen, frames_color, rect,
                            2)
            pygame.display.flip()