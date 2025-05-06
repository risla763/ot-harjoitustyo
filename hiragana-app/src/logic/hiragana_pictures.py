import os
import pygame 
import random

class HiraganaPictureLogic():
    """Luokka joka saa hiraganan kuvat listaan, joka sisältää tupleja joissa on
    hiragana ja sitä vastaava tavu. Myös sekoittaa listan, jolloin kun pelin aloittaa
    alusta hiraganat ovat eri järjestyksessä.
    """
    def __init__(self):
        """Luokan konstruktori, joka alustaa pygamen, luo listan, johon hiraganat menevät
        sekä tekee listan, jossa ovat tavut, jotka vastaavat hiraganoja.
        """
        pygame.init()
        self.list_of_hiraganas = []
        self.list_of_letters = ["a", "u", "i", "e", "o", "ka","ki","ku","ke",
        "ko", "sa", "shi", "su", "se", "so", "ta"]

    def list_hiraganas(self):
        """"Metodi, jossa haetaan jokainen hiraganakuva niihin johtavan polun avulla ja
        lisätään konstruktorissa luotuun listaan. Listaan myös lisätään tuplemaisesti 
        hiraganakuvan kanssa tavu.
        Returns: palauttaa sekoitetun listan, jossa jokainen hiraganakuva sekä tavu tuplena."""
        for i in self.list_of_letters:
            hiragana_directory = 'src/PNG-hiragana_letters'
            path_to_hiragana = os.path.join(hiragana_directory, f"Hiragana_{i}.png")
            hiragana_image = pygame.image.load(path_to_hiragana)
            self.list_of_hiraganas.append((hiragana_image,{i}))
        return self.shuffle_hiraganas()

    def shuffle_hiraganas(self):
        #tarviiko tätä edes?
        """Sekoitetaan hiraganat listassa
        Returns: palauttaa sekoitetun listan hiraganoja"""
        random.shuffle(self.list_of_hiraganas)
        return self.list_of_hiraganas
