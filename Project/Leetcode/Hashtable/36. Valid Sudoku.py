class Solution(object):
    def isValidSudoku(self, board):
        return self.isValidCol(board) and self.isValidNineCell(board) and self.isValidRow(board)

    def isValidRow(self, board):
        for r in range(len(board)):
            row = [x for x in board[r] if x != '.']
            if len(set(row)) != len(row): return False
        return True

    def isValidCol(self, board):
        ls = len(board)
        for c in range(ls):
            col = [board[r][c] for r in range(ls) if board[r][c] != '.']
            if len(set(col)) != len(col): return False
        return True

    def isValidNineCell(self, board):
        ls = len(board)
        for r in range(0, ls, 3):
            for c in range(0, ls, 3):
                temp = []
                for i in range(3):
                    for j in range(3):
                        num = board[r + i][c + j]
                        if num != '.': temp.append(num)
                if len(set(temp)) != len(temp): return False
        return True