import pygame

class Rect:
    @staticmethod

    def make_changing_rect(text, text_color, surface_color, frames_color, screen):
        font = pygame.font.SysFont(None, 77)
        surface = font.render(str(text), True, text_color)

        rect = pygame.Rect(1590, 15, 100, 70)  # tee näistä omat muuttujat

        # estää numeroiden menemisen toistensa pälle
        rect_surface = screen.subsurface(rect)
        rect_surface.fill(surface_color)  # estää numeroiden päällekkäisyyden
        screen.blit(surface, rect)  # tällä pitäisi saada teksti näytölle
        pygame.draw.rect(screen, frames_color, rect,
                         2)  # (0,0,0) reunusten väri
        pygame.display.flip()
