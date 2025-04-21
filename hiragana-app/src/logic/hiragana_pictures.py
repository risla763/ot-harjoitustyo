import pygame 
import random
import os

class HiraganaPictureLogic():
    def __init__(self):
        pygame.init()
        self.list_of_hiraganas = []
        self.list_of_letters = ["a", "u", "i", "e", "o", "ka","ki","ku","ke", 
        "ko", "sa", "shi", "su", "se", "so", "ta"]

    def list_hiraganas(self):
        for i in self.list_of_letters:
            hiragana_directory = 'src/PNG-hiragana_letters'
            path_to_hiragana = os.path.join(hiragana_directory, f"Hiragana_{i}.png")
            hiragana_image = pygame.image.load(path_to_hiragana)
            self.list_of_hiraganas.append((hiragana_image,{i}))
        return self.shuffle_hiraganas()

    def shuffle_hiraganas(self):
        random.shuffle(self.list_of_hiraganas)
        return self.list_of_hiraganas



