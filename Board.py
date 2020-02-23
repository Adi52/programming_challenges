
class Board():
    def __init__(self, user_choice):
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0]]
        self.user_choice = user_choice
        self.ROW_COUNT = 6
        self.COLUMN_COUNT = 7

    def display_board(self):
        print(" 1  2  3  4  5  6  7")
        for i in self.board:
            print(i)

    def get_next_open_row(self):
        result = -1
        for i in range(self.ROW_COUNT):
            if self.board[i][self.user_choice - 1] == 0:
                result += 1
        return result

    def drop_piece(self, piece):
        row = self.get_next_open_row(self.board, self.user_choice)
        self.board[row][self.user_choice - 1] = piece

    def is_valid_location(self):
        return self.board[0][self.user_choice - 1] == 0

