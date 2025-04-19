import pygame 
import random
import os

class HiraganaPictureLogic():
    def __init__(self, screen):
        pygame.init()

        # tämä alempana on ui
        self.screen = screen
        self.list_of_hiraganas = []


        #jokaiselle kirjaimelle myös numero että niitä kuvia voidaan sattumalla laittaa näytölle

    def list_hiraganas(self):
        list_of_letters = ["a", "u", "i", "e"]
        for i in list_of_letters: #0-3 eli 4
            self.one_hiragana_to_list(i)
        #kun kaikki hiraganat listattu niin shufflee  ja piirtää uuden:
        random.shuffle(self.list_of_hiraganas)
        image = self.list_of_hiraganas[0]
        self.screen.blit(image,(0,0))
        pygame.display.flip()

    def one_hiragana_to_list(self, i):
        hiragana_directory = 'src/PNG-hiragana_letters'
        path_to_hiragana = os.path.join(hiragana_directory, f"Hiragana_{i}.png")
        hiragana_image = pygame.image.load(path_to_hiragana)
        #tee listatsa tuple, jossa kirjainyhdistelmä ja hiragana (voidaan käyttää tarkistamisessa)
        self.list_of_hiraganas.append(hiragana_image)



