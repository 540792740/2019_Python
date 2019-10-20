class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.dfs(res, s)
        return res
    def dfs(self, res, s, subset = []):
        if not s:
            res.append(subset)

        ls = len(s)
        for i in range(1, ls + 1):
            if s[:i] == s[:i][::-1] and len(s[:i]) == i:
                self.dfs(res, s[i:], subset + [s[:i]])

if __name__ == '__main__':
    S = Solution()
    # test = S.partition('aabb')
    test = S.partition('aab')
    print(test)