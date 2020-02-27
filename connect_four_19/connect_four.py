import random
import pygame
import pygame.gfxdraw
import sys
import time
from math import floor
from settings import Settings
from board_class import Board
from filledrounded_rect import AAfilledRoundedRect
from piece import Piece

board = Board()
turn = 0


def bot_choice():
    return random.randint(0, 6)


def user_choice_def(event):
    user_choice = event.pos[0]
    user_choice = int(floor(user_choice / 100))
    if user_choice > 6:
        user_choice = 6
    return user_choice


def check_events(ai_settings, screen, game_over):
    # Reakcja na zdarzenia generowane przez klawiaturę i mysz.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            posx = event.pos[0]
            pygame.gfxdraw.filled_circle(screen, posx, 50, 42, (139, 124, 0))

            pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            perform_turn(event, ai_settings, screen, game_over)
            global turn
            turn += 1




def update_screen(ai_settings, screen, piece):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
    # odswiezenie ekranu w trakcie kazdej iteracji
    screen.fill(ai_settings.bg_color)
    # Stworzenie tablicy w pygame + cień
    AAfilledRoundedRect(screen, pygame.Rect(4, 97, 740, 650), (37, 67, 166), radius=0.04)
    AAfilledRoundedRect(screen, pygame.Rect(1, 100, 740, 650), (0, 123, 255), radius=0.04)

    for column in range(board.COLUMN_COUNT):
        for row in range(board.ROW_COUNT):
            if board.board[row][column] == 0:
                piece.draw(column, row, ai_settings.bg_color)
            elif board.board[row][column] == 1:
                piece.draw(column, row, (139, 124, 0))
            else:
                piece.draw(column, row, (139, 0, 0))

    # wyświetlanie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()


def perform_turn(event, ai_settings, screen, game_over):
    global turn
    turn = turn % 2
    if turn == 0:
        user_choice = user_choice_def(event)

    elif turn == 1:
        user_choice = bot_choice()


    if board.is_valid_location(user_choice):
        board.drop_piece(user_choice, turn + 1)
        #board.display_board()

        if board.winning_condition(turn):
            print('Wygrana gracza {}!'.format(turn + 1))
            game_over = True



    if game_over:
        pygame.time.wait(5000)


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    piece = Piece(screen, board, ai_settings)
    pygame.display.set_caption("Connect four")
    game_over = False

    while not game_over:
        update_screen(ai_settings, screen, piece)
        check_events(ai_settings, screen, game_over)


run_game()
