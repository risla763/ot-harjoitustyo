from objects.button_rect import ButtonRect
from ui.button_ui import Buttons
from ui.game_screen import GameScreen
from ui.menu_screen_ui import MenuScreen
from logic.hiragana_pictures import HiraganaPictureLogic
import pygame

#tehtävälista
#pylint
#testit
#arkkitehtuuri
#toimiiko .gitignore

pygame.init()
screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Hiragana learning app')

MenuScreen().game_menu_screen(screen)

run = True
game_menu_screen_boolean = True
game_screen_boolean = False
scoreboard_screen = False

start_game_button = Buttons(screen).make_rect("start game",(200, 200, 190, 40))
scoreboard_button = Buttons(screen).make_rect("score board",(400, 200, 190, 40))
#tämä alempi vain koska sellainen tarvitaan, mutta ongelma, miten se saada näkyviin vasta kun näyttö vaihtuu

input_field_button = Buttons(screen).make_rect("score board",(400, 200, 190, 40))


input_active = False
font = pygame.font.Font(None, 32)
user_text = ''

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            while game_menu_screen_boolean:
                MenuScreen().game_menu_screen(screen) #onko tarvittava
                if start_game_button.collidepoint(pygame.mouse.get_pos()):
                    GameScreen().game_screen(screen)
                    GameScreen().make_input_field((500, 400, 190, 50), screen)
                    game_menu_screen_boolean = False     
                    game_screen_boolean = True      
                    pygame.display.flip() #onko tarvittava

                elif scoreboard_button.collidepoint(pygame.mouse.get_pos()):
                    GameScreen().game_screen(screen)
                    game_menu_screen_boolean = False
                    scoreboard_screen = True
                
                else:
                    break


                #tämä alempi vasta aktiivinen kun peli käynnistetty
                #käytänkö edes?
        
        if event.type == pygame.KEYDOWN:
            if game_screen_boolean:

                user_text += event.unicode
                print("moi")

                text_surface = font.render(user_text, True, (173, 216, 230))
                screen.blit(text_surface,(500,400))

                #jos painaa enteriä....tarkistaa onko oikea kirjain..

    pygame.display.flip() 


pygame.quit()
raise SystemExit