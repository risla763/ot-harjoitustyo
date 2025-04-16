import pygame 

class HiraganaPictureLogic():
    def __init__(self, screen):
        pygame.init()
        image = pygame.image.load('src/PNG-hiragana_letters/Hiragan_u.png')
        screen.blit(image,(0,0))
        pygame.display.flip()

        #jokaiselle kirjaimelle myös numero että niitä kuvia voidaan sattumalla laittaa näytölle
