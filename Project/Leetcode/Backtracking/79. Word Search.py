'''
exist1 is better than exist:
using index rather than change word -- word[1:]


'''

class Solution(object):
    def exist1(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def preCheck():
            # Build Check Dic
            preDic = {}
            for i in word:
                if i in preDic:
                    preDic[i] += 1
                else:
                    preDic[i] = 1

            # Check is there over alpha in word
            for i in board:
                for j in i:
                    if j in preDic and preDic[j] > 0:
                        preDic[j] -= 1

            # for i in preDic.values():
            #     if i > 0: return False
            return True


        def helper(word_index, x, y):
            if board[x][y] != word[word_index]:
                return False
            elif word_index == ls - 1: return True
            else:
                word_index += 1
                tempChar = board[x][y]
                board[x][y] = None
                for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x_next = x + d[0]
                    y_next = y + d[1]
                    if -1 < x_next < m and -1 < y_next < n and board[x_next][y_next]:
                        if helper(word_index, x_next, y_next):
                            return True
                board[x][y] = tempChar
                return False

        if not board: return False
        if not word: return True
        if not preCheck(): return False

        m = len(board)
        n = len(board[0])
        ls = len(word)

        for i in range(m):
            for j in range(n):
                if helper(0, i, j):
                    return True
        return False
    # 23%
    def exist(self, board, word):
        if not board: return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0: return True
        if i < 0 or  i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        # Avoid visited again
        temp = board[i][j]
        board[i][j] = '#'
        direction = ((0, 1), (1, 0), (-1, 0), (0, -1))
        for dx, dy in direction:
            x = i + dx
            y = j + dy
            res = self.dfs(board, x, y, word[1:])
            if res == True: return True
            else: continue
        board[i][j] = temp
        return False


if __name__ == '__main__':
    S = Solution()
    test = S.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    test = S.exist([["a"]], "ab")
    print(test)