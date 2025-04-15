from objects.buttons import Button
from ui.make_rect import Rect
from ui.game_screen import GameScreen
from ui.menu_screen_ui import MenuScreen
import pygame

pygame.init()

screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Hiragana learning app')

#pylint


#nämä kaksi alempaa muaalle (NIMEÄ KANSIOT HYVIN!)
def game_screen(screen):
    screen.fill((0, 0, 0))  
    font = pygame.font.SysFont(None, 50)
    text_surface = font.render("Game comes here", True, (173, 216, 230))
    screen.blit(text_surface, (200, 200))
    pygame.display.flip()


MenuScreen().game_menu_screen(screen)

run = True
game_menu_screen_boolean = True
game_screen_boolean = False
scoreboard_screen = False

start_game_button = Rect(screen).make_rect("start game",(200, 200, 190, 40))
scoreboard_button = Rect(screen).make_rect("score board",(400, 200, 190, 40))
#tämä alempi vain koska sellainen tarvitaan, mutta ongelma, miten se saada näkyviin vasta kun näyttö vaihtuu
input_field_button = Rect(screen).make_rect("score board",(400, 200, 190, 40))


input_active = False
font = pygame.font.Font(None, 32)
user_text = ''

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            while game_menu_screen_boolean:
                MenuScreen().game_menu_screen(screen)
                if start_game_button.collidepoint(pygame.mouse.get_pos()):
                    game_screen(screen)
                    game_menu_screen_boolean = False
                    #game_screen_boolean = True
                    pygame.display.flip() 

                elif scoreboard_button.collidepoint(pygame.mouse.get_pos()):
                    game_screen(screen)
                    game_menu_screen_boolean = False
                    scoreboard_screen = True
                
                else:
                    break


                #tämä alempi vasta aktiivinen kun peli käynnistetty
                #otin mallia chatgpt:ltä mutta vain joissain kohdissa??
                #käytänkö edes?
            while game_screen_boolean:
                game_screen(screen)
                if input_field_button.collidepoint(pygame.mouse.get_pos()):
                    text = ""
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                            print("enter painettu")
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                #
        if event.type == pygame.KEYDOWN:
            user_text += event.unicode
            print("moi")

            text_surface = font.render(user_text, True, (255,255,255))
            screen.blit(text_surface,(0,0))


    pygame.display.flip() 


pygame.quit()
raise SystemExit