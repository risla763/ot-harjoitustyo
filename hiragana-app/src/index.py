import pygame
from ui.button_ui import Buttons
from ui.game_screen import GameScreen
from ui.menu_screen_ui import MenuScreen
from logic.hiragana_pictures import HiraganaPictureLogic
from logic.answers import CheckAndReviev
from database.make_database import DB


DB().make_table()

#tehtävälista:
#pylint
#testit
#arkkitehtuuri!!
#.gitignore
#dokumentatointi kesken
#coveragerg tiedostoon kaikki mitä coverage raporttiin ei haluta ja coverage raport
#scoreboard ja sql, johon ainakin korkein score
#käyttäjätunnus ja kirjautuminen
#tarkista onko toi disable= no-member hyvä
#vaihda exit game napin paikkaa

pygame.init()  # pylint: disable=no-member
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Hiragana learning app')
highest_score = 0

MenuScreen().game_menu_screen(screen)

RUN = True
GAME_MENU_SCREEN_BOOLEAN = True
GAME_SCREEN_BOOLEAN = False
SCOREBOARD_SCREEN = False

start_game_button = Buttons(screen).make_rect("start game",(200, 200, 190, 40))
scoreboard_button = Buttons(screen).make_rect("score board",(400, 200, 190, 40))
#exit_game_button = Buttons(screen).make_rect("Exit game",(700, 200, 200, 40))

font = pygame.font.Font(None, 32)
USER_TEXT = ''
text_surface = font.render(USER_TEXT, True, (173, 216, 230)) #ui
score = 0

#muuta tuo ylempi sql queryksi

while RUN:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pylint: disable=no-member
            RUN = False

        if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
            while GAME_MENU_SCREEN_BOOLEAN:
                MenuScreen().game_menu_screen(screen) #onko tarvittava
                if start_game_button.collidepoint(pygame.mouse.get_pos()):
                    GameScreen(screen).game_screen()
                    exit_game_button = Buttons(screen).make_rect("Exit game",(700, 200, 200, 40))
                    hiraganas = HiraganaPictureLogic().list_hiraganas()
                    hiragana_tuple = GameScreen(screen).draw_hiragana(hiraganas)
                    GameScreen(screen).make_input_field((500, 400, 190, 50), screen)
                    GAME_MENU_SCREEN_BOOLEAN = False
                    GAME_SCREEN_BOOLEAN = True
                    pygame.display.flip() #onko tarvittava

                elif scoreboard_button.collidepoint(pygame.mouse.get_pos()):
                    GameScreen(screen).game_screen()
                    GAME_MENU_SCREEN_BOOLEAN = False
                    SCOREBOARD_SCREEN = True
                else:
                    break

        if event.type == pygame.KEYDOWN: # pylint: disable=no-member
            if GAME_SCREEN_BOOLEAN:
                if event.key == pygame.K_BACKSPACE: #jos pitää K_BACKSPACEN alhaalla kumittaako?
                    #tee tälle raja jos user_text on pitempi kuin inputfield ei voi enää kirjottaa
                    #vähön välkkyy ja glitchaa teksti kun kirjoitan
                    if USER_TEXT != '':
                        USER_TEXT = USER_TEXT[:-1]
                        screen.blit(text_surface,(500,400))
                    else:
                        continue
                elif event.key == pygame.K_RETURN:
                    answer, score = CheckAndReviev(hiraganas).check_answer(hiragana_tuple, USER_TEXT, screen, score)
                    hiragana_tuple = GameScreen(screen).draw_hiragana(hiraganas)
                    USER_TEXT = ''
                else:
                    USER_TEXT += event.unicode
                #tämä alla oleva koodi aiheuttaa flickering..voiko korjata
                GameScreen(screen).make_input_field((500, 400, 190, 50), screen)
                #
                text_surface = font.render(USER_TEXT, True, (173, 216, 230)) #ui?
                screen.blit(text_surface,(500,400)) #tämä päivittää siirrä ui osastoon
                pygame.display.flip() #ehkä turha

    if event.type == pygame.MOUSEBUTTONDOWN: # pylint: disable=no-member
        if GAME_SCREEN_BOOLEAN:
            if exit_game_button.collidepoint(pygame.mouse.get_pos()):
                MenuScreen().game_menu_screen(screen) 
                DB().insert(score)
                highest_score = DB().fetch_from_scoreboard()
                GAME_MENU_SCREEN_BOOLEAN = True
                GAME_SCREEN_BOOLEAN = False
                score = 0
                start_game_button = Buttons(screen).make_rect("start game",(200, 200, 190, 40))
                scoreboard_button = Buttons(screen).make_rect("score board",(400, 200, 190, 40))
        

    pygame.display.flip()

pygame.quit() # pylint: disable=no-member
raise SystemExit
