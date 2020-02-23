
class Board():

    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]

        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7

    def display_board(self):
        print(" 1  2  3  4  5  6  7")
        for i in self.board:
            print(i)

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

