import time
import random
import pygame
import pygame.gfxdraw
import sys
from settings import Settings
from board_class import Board
from filledrounded_rect import AAfilledRoundedRect
from piece import Piece


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
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)


def update_screen(ai_settings, screen):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
    # odswiezenie ekranu w trakcie kazdej iteracji
    screen.fill(ai_settings.bg_color)
    #Stworzenie tablicy w pygame + cień
    AAfilledRoundedRect(screen, pygame.Rect(4, 97, 740, 650), (37, 67, 166), radius=0.04)
    AAfilledRoundedRect(screen, pygame.Rect(1, 100, 740, 650), (0, 123, 255), radius=0.04)
    piece = Piece(screen, board, ai_settings)

    for column in range(board.COLUMN_COUNT):
        for row in range(board.ROW_COUNT):
            piece.draw(column, row, ai_settings.bg_color)

    # wyświetlanie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Connect four")

    while True:
        check_events(ai_settings, screen)

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
                update_screen(ai_settings, screen)
            else:
                print('Już jest pełno!')
                time.sleep(3)

            # cls()




run_game()
