import collections

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row = [0] * n
        self.col = [0] * n
        self.diag1 =0
        self.diag2 = 0
        self.n = n

    def move(self, row, col, player):
        if player == 1: offset = 1
        else: offset = -1

        # Get the sum of each row and each col
        self.row[row] += offset
        self.col[col] += offset

        # Diagonal
        if row == col:
            self.diag1 += offset
        if row + col == self.n - 1:
            print(row, col, self.n)

            self.diag2 += offset

        if self.n in [self.row[row], self.col[col], self.diag2, self.diag1]:
            return 1
        if -self.n in [self.row[row], self.col[col], self.diag2, self.diag1]:
            return 2
        return 0


S = TicTacToe(3)
S.move(0,0,1)
S.move(0,2,2)
S.move(2,2,1)
S.move(1,1,2)
S.move(2,0,1)
S.move(1,0,2)
S.move(2,1,1)