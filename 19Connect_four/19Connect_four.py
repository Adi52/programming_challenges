import time
from board import Board


"""
ROW_COUNT = 6
COLUMN_COUNT = 7

board = [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]]

def display_board(board):
    print(" 1  2  3  4  5  6  7")
    for i in board:
        print(i)

def drop_piece(board, user_choice, piece):
    row = get_next_open_row(board, user_choice)
    board[row][user_choice-1] = piece


def is_valid_location(board, user_choice):
    return board[0][user_choice-1] == 0

def get_next_open_row(board, user_choice):
    result = -1
    for i in range(ROW_COUNT):
        if board[i][user_choice-1] == 0:
            result += 1
    return result
"""
board = Board()


def incorrect_input():
    print('Możesz wpisać tylko liczbę 1-7!')
    time.sleep(2)


game_over = False

print('Zaczynaj! wybierz kolumne 1-7 w którą chcesz wrzucić żeton.')
print('X - Ty')
print('Y - przeciwnik')
while not game_over:
    board.display_board()

    try:
        user_choice = int(input("Wybieram: "))
        if user_choice > 7 or user_choice < 1:
            incorrect_input()
            continue
    except ValueError:
        incorrect_input()
        continue

    if board.is_valid_location(user_choice):
        board.drop_piece(user_choice, 1)
    else:
        print('Już jest pełno!')


#Musisz dodać użytkownika, zrób refaktoryzację i odwołanie do jednej funkcji sprawdzającej
#Potem dodaj warunek wygranej: 4 na skos, 4 pion, 4 poziom


