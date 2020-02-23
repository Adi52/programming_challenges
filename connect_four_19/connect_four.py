import time
import random
from board_class import Board

board = Board()


def incorrect_input():
    print('Możesz wpisać tylko liczbę 1-7!')
    time.sleep(2)


def bot_choice():
    return random.randint(1, 7)


game_over = False
turn = 0

print('Zaczynaj! wybierz kolumne 1-7 w którą chcesz wrzucić żeton.')
print('X - Ty')
print('Y - przeciwnik')
while not game_over:
    turn = turn % 2
    board.display_board()
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
        board.drop_piece(user_choice, turn+1)
    else:
        print('Już jest pełno!')

    time.sleep(2)
    turn += 1

# Potem dodaj warunek wygranej: 4 na skos, 4 pion, 4 poziom
