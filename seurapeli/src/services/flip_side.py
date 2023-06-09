import os
import pygame

class Flip:
    """This class draws the back of the cards.
    Attributes:
        screen: diplays the pygame screen."""
    def __init__(self, screen):
        """This is the constructor of the class and it retrieves a png file with the image
        of the back side of a card
        Args:
            screen: displays the pygame screen."""
        self.screen = screen
        png_directory = "src/services/entities/PNG-cards-1.3"
        file2 = os.path.join(png_directory,"10_of_hearts.png")
        self.image3 = pygame.image.load(file2)
        file = os.path.join(png_directory,"pngegg.png")
        self.image2 = pygame.image.load(file)
        self.rect = self.image2.get_rect()
        self.scaling()
        self.image_width_scaling()
    def scaling(self):
        """This method retrieves the height of the image """
        self.image_height = self.image3.get_height()
    def image_width_scaling(self):
        """This method retrieves the width of the image"""
        self.image_width = self.image3.get_width()
    def draw(self, surface, pos):
        """This method draws the back side of a card on the screen
        Args:
            surface: screen that displays the pygame
            pos: tuple at which the reverse side of the image is drawn""" #siirrä ui
        scaled_image2 = pygame.transform.scale(self.image2,
                                                (self.image_width+90,self.image_height+90))
        self.rect.topleft = pos
        surface.blit(scaled_image2, self.rect)
        