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
