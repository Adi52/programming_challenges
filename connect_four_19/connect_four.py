import time
import random
import pygame
from settings import Settings
from board_class import Board
import game_functions

board = Board()

cls = lambda: print('\n' * 1000)

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Connect four")

    while True:
        print('Zaczynaj! wybierz kolumne 1-7 w którą chcesz wrzucić żeton.')
        print('1 - Ty')
        print('2 - przeciwnik')
        board.display_board()
        game_functions.start_game()




            #cls()

run_game()


# Potem dodaj warunek wygranej: 4 na skos, 4 pion, 4 poziom
