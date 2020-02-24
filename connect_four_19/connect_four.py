import time
import random
import pygame
import sys
from settings import Settings
from board_class import Board

board = Board()

cls = lambda: print('\n' * 1000)


def incorrect_input():
    print('Możesz wpisać tylko liczbę 1-7!')
    time.sleep(2)


def bot_choice():
    return random.randint(1, 7)


def check_events(ai_settings, screen):
    """Reakcja na zdarzenia generowane przez klawiaturę i mysz."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
    # odswiezenie ekranu w trakcie kazdej iteracji
    screen.fill(ai_settings.bg_color)
    pygame.draw.rect(screen, (0, 123, 255), pygame.Rect(0, 114, 800, 600))

    # wyświetlanie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Connect four")

    while True:
        check_events(ai_settings, screen)

        """
        game_over = False
        turn = 0

        print('Zaczynaj! wybierz kolumne 1-7 w którą chcesz wrzucić żeton.')
        print('1 - Ty')
        print('2 - przeciwnik')
        board.display_board()
        while not game_over:
            turn = turn % 2

            if turn == 0:
                try:
                    user_choice = int(input("Wybieram: "))
                    if user_choice > 7 or user_choice < 1:
                        incorrect_input()
                        continue
                except ValueError:
                    incorrect_input()
                    continue
            if turn == 1:
                user_choice = bot_choice()

            if board.is_valid_location(user_choice):
                board.drop_piece(user_choice, turn + 1)
                board.display_board()

                if board.winning_condition(turn):
                    print('Wygrana gracza {}!'.format(turn + 1))
                    game_over = True

                turn += 1
                time.sleep(1)

            else:
                print('Już jest pełno!')
                time.sleep(3)

            # cls()
            """
        update_screen(ai_settings, screen)


run_game()
