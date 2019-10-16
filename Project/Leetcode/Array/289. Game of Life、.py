'''
0. 0 --> 2 if dead cell alive, to make %2 == 0
1. 1 --> 3 if alive cell dead, to make %2 == 1
'''

class Solution(object):
    def gameOfLife(self, board):
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    count = self.nnb(board, i, j)
                    if count == 3:
                        board[i][j] = 2
                else:
                    count = self.nnb(board, i, j)
                    if count < 2 or count > 3:
                        board[i][j] = 3

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0
        return board

    def nnb(self, board, i, j):
        count = 0
        m, n = len(board), len(board[0])
        neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        # if i - 1 > 0 and j - 1 > 0:
        # count += board[i - 1][j - 1] % 2
        for d in neighbors:
            if 0 <= i + d[0] < m and 0 <= j + d[1] < n:
                count += board[i + d[0]][j + d[1]] % 2
        return count


if __name__ == '__main__':
    S = Solution()
    a = S.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
    print(a)