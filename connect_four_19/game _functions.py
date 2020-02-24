import random
import time

import board


def get_next_open_row(self, user_choice):
    result = -1
    for i in range(self.ROW_COUNT):
        if self.board[i][user_choice - 1] == 0:
            result += 1
    return result


def drop_piece(self, user_choice, piece):
    row = self.get_next_open_row(user_choice)
    self.board[row][user_choice - 1] = piece


def is_valid_location(self, user_choice):
    return self.board[0][user_choice - 1] == 0


def winning_condition(self, turn):
    # horizontal
    for column in range(self.COLUMN_COUNT - 3):
        for row in range(self.ROW_COUNT):
            if (self.board[row][column] == turn + 1 and self.board[row][column + 1] == turn + 1 and
                    self.board[row][column + 2] == turn + 1 and self.board[row][column + 3] == turn + 1):
                return True
    # vertical
    for column in range(self.COLUMN_COUNT):
        for row in range(self.ROW_COUNT - 3):
            if (self.board[row][column] == turn + 1 and self.board[row + 1][column] == turn + 1 and
                    self.board[row + 2][column] == turn + 1 and self.board[row + 3][column] == turn + 1):
                return True

    # positively slopped diagonals
    for column in range(self.COLUMN_COUNT - 3):
        for row in range(self.ROW_COUNT - 3):
            if (self.board[row][column] == turn + 1 and self.board[row + 1][column + 1] == turn + 1 and
                    self.board[row + 2][column + 2] == turn + 1 and self.board[row + 3][column + 3] == turn + 1):
                return True

    # negatively slopped diagonals
    for column in range(self.COLUMN_COUNT - 3):
        for row in range(self.ROW_COUNT - 3):
            if (self.board[row][column] == turn + 1 and self.board[row + 1][column + 1] == turn + 1 and
                    self.board[row + 2][column + 2] == turn + 1 and self.board[row + 3][column + 3] == turn + 1):
                return True

def incorrect_input():
    print('Możesz wpisać tylko liczbę 1-7!')
    time.sleep(2)


def bot_choice():
    return random.randint(1, 7)

def start_game():
    game_over = False
    turn = 0
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

        if is_valid_location(user_choice):
            drop_piece(user_choice, turn + 1)
            board.display_board()

            if winning_condition(turn):
                print('Wygrana gracza {}!'.format(turn + 1))
                game_over = True

            turn += 1
            time.sleep(1)

        else:
            print('Już jest pełno!')
            time.sleep(3)