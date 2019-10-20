class Solution(object):


    # 50%
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        res = []
        self.dfs(k, n, res, [], 1)
        return res
    def dfs(self, k, n, res, subset, index):
        if k == 0 and subset[0] != subset[1]:
            res.append(subset)
            return
        for i in range(index, n + 1):
            self.dfs(k - 1, n, res, subset + [i], i + 1)

if __name__ == '__main__':
    S = Solution()
    # test = S.combine(2,1)
    # test = S.combine(4,2)
    test = S.combine(3,3)
    print(test)