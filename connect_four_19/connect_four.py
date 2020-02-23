import time
from board_class import Board


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




#Potem dodaj warunek wygranej: 4 na skos, 4 pion, 4 poziom


