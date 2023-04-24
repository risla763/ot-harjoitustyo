import os
import pygame
from card_deck import Card

class Flip:
    def __init__(self, screen):
        self.screen = screen
        png_directory = "PNG-cards-1.3"
        file2 = os.path.join(png_directory,"10_of_hearts.png")
        self.image3 = pygame.image.load(file2)
        file = os.path.join(png_directory,"pngegg.png")
        self.image2 = pygame.image.load(file)
        self.rect = self.image2.get_rect()
        self.scaling()
        self.image_width_scaling()
        
    def scaling(self):
        self.image_height = self.image3.get_height()
        
    def image_width_scaling(self):
        self.image_width = self.image3.get_width()
        
    def draw(self, surface, pos):
        new_size = (700, 700)
        scaled_image2 = pygame.transform.scale(self.image2, (self.image_width+90,self.image_height+90))
        self.rect.topleft = pos
        print(type(surface))
        surface.blit(scaled_image2, self.rect)
        