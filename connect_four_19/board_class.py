
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
        print("1 2 3 4 5 6 7")
        for i in self.board:
            print(*i, sep='|')

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
        #horizontal
        for column in range(self.COLUMN_COUNT-3):
            for row in range(self.ROW_COUNT):
                if (self.board[row][column] == turn + 1 and self.board[row][column+1] == turn + 1 and
                        self.board[row][column+2] == turn + 1 and self.board[row][column+3] == turn + 1):
                    return True
        #vertical
        for column in range(self.COLUMN_COUNT):
            for row in range(self.ROW_COUNT-3):
                if (self.board[row][column] == turn + 1 and self.board[row+1][column] == turn + 1 and
                        self.board[row+2][column] == turn + 1 and self.board[row+3][column] == turn + 1):
                    return True

        #positively slopped diagonals
        for column in range(self.COLUMN_COUNT-3):
            for row in range(self.ROW_COUNT-3):
                if (self.board[row][column] == turn + 1 and self.board[row+1][column+1] == turn + 1 and
                        self.board[row+2][column+2] == turn + 1 and self.board[row+3][column+3] == turn + 1):
                    return True

        #negatively slopped diagonals
        for column in range(self.COLUMN_COUNT-3):
            for row in range(self.ROW_COUNT-3):
                if (self.board[row][column] == turn + 1 and self.board[row+1][column+1] == turn + 1 and
                        self.board[row+2][column+2] == turn + 1 and self.board[row+3][column+3] == turn + 1):
                    return True