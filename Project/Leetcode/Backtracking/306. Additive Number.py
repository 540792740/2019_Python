class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        return self.dfs(num, [])
    def dfs(self, num, subset):
        print(subset)
        if len(subset) >= 3 and subset[-1] != subset[-2] + subset[-3]:
            return False
        if not num and len(subset) >= 3:
            return True
        ls = len(num)
        for i in range(1, ls + 1):
            cur = num[:i]
            if cur[0] == '0' and len(cur) != 1:
                continue
            if self.dfs(num[i:], subset + [int(cur)]):
                return True
        return False

if __name__ == '__main__':
    S = Solution()
    test = S.isAdditiveNumber("112358")
    test = S.isAdditiveNumber("0000")
    test = S.isAdditiveNumber("")
    test = S.isAdditiveNumber("1")
    test = S.isAdditiveNumber("111")
    # test = S.isAdditiveNumber("11001100")
    print(test)