class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        res = 0
        row = len(M)
        col = len(M[0])
        arr = []
        for i in range(row):
            for j in range (col) :
                arr = []
                if M[i][j] == 1:
                    res += 1
                    self.dfs(arr, M, i,j)

        return res
    def dfs(self,arr, M, i, j):
        for x1 in range(i, len(M)):
            if M[x1][j] == 1 and x1 not in arr:
                M[x1][j] = 0
                arr.append(x1)
                self.dfs(arr, M, i, x1)
            if M[x1][j] == 1:
                M[x1][j] = 0
if __name__ == '__main__':
    S = Solution()
    a = S.findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
    # a = S.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
    print(a)