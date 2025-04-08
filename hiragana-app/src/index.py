from objects.buttons import Button
from ui.game_menu_screen import StartingScreen
import pygame

pygame.init()

screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Hiragana learning app')

#button stuff 
width, height = 640, 480

#lisää fontti alempaan

#testi screenin vaihto ja tämä myös tulee muualle
def game_screen(screen):
    screen.fill((0, 0, 0))  
    font = pygame.font.SysFont(None, 50)
    text_surface = font.render("Game comes here", True, (173, 216, 230))
    screen.blit(text_surface, (200, 200))
    pygame.display.flip()

screen.fill("purple")
run = True
game_menu_screen = True

#tämä siirtyy muualle:
#start_game_button = Button().make_rect("Start game ",
                                                 #  (255, 182, 193), (255, 255, 255),
                                                  # (200, 200, 190, 40), screen)
start_game_button = StartingScreen(screen).make_rect()

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False




   
    if event.type == pygame.MOUSEBUTTONDOWN:
        while game_menu_screen:
            if start_game_button.collidepoint(pygame.mouse.get_pos()):
                game_screen(screen)
                game_menu_screen = False
                #pygame.display.flip() 
                print("klikattu nappia")
        


    #pygame.display.flip() 


pygame.quit()
raise SystemExit