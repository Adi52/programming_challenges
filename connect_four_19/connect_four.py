import random
import pygame
import pygame.gfxdraw
import sys, time
from math import floor
from settings import Settings
from board_class import Board
from filledrounded_rect import AAfilledRoundedRect
from piece import Piece

board = Board()

is_player_turn = True

def bot_choice():
    return random.randint(0, 6)


def user_choice_def(event):
    user_choice = event.pos[0]
    user_choice = int(floor(user_choice / 100))
    if user_choice > 6:
        user_choice = 6
    return user_choice


def check_events(screen, game_over, ai_settings, piece):
    # Reakcja na zdarzenia generowane przez klawiaturę i mysz.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            posx = event.pos[0]
            pygame.gfxdraw.aacircle(screen, posx, 50, 42, (139, 124, 0))
            pygame.gfxdraw.filled_circle(screen, posx, 50, 42, (139, 124, 0))
            pygame.display.flip()

        if event.type == pygame.MOUSEBUTTONDOWN:
            perform_turn(user_choice_def(event), 1, game_over, ai_settings, screen, piece)


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


def perform_turn(choice, who, game_over, ai_settings, screen, piece):
    if board.is_valid_location(choice):
        board.drop_piece(choice, who + 1)
        #board.display_board()

        if board.winning_condition(who):
            message = 'Wygrana gracza {}!'.format(who + 1)
            update_screen(ai_settings, screen, piece)
            time.sleep(0.5)

            game_over = True

    if game_over:
        time.sleep(4)
        sys.exit()


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    piece = Piece(screen, board, ai_settings)
    pygame.display.set_caption("Connect four")
    game_over = False

    while not game_over:
        update_screen(ai_settings, screen, piece)
        if is_player_turn:
            check_events(screen, game_over, ai_settings, piece)
        else:
            perform_turn(bot_choice(), 0, game_over, ai_settings, screen, piece)
        is_player_turn != is_player_turn

run_game()
