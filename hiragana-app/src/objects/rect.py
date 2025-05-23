import pygame

class ButtonRect():
#VAIHDA TÄMÄN NIMI VAAN MAKE RECT KANSIOKSI
    def make_rect(self,text, text_color, surface_color, rect_position, screen):

        font = pygame.font.SysFont(None, 50)
        #muuta polku johonkin entities..missä hiraganat myös on..ne pitää myös siirtää
        font = pygame.font.Font('src/ChakraPetch-Bold.ttf', 30)
        surface = font.render(str(text), True, text_color)
        rect = pygame.Rect(rect_position)

        rect_surface = screen.subsurface(rect)
        rect_surface.fill(surface_color)

        screen.blit(surface, rect.topleft)
        pygame.draw.rect(screen, surface_color , rect, 2)

        pygame.display.flip()

        return rect
