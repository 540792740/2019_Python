class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(res, '', s, 4)
        return res
    def dfs(self, res, subset, s, index):
        ls = len(s)
        if index == 0 and ls == 0 :
            res.append(subset[:len(subset) - 1])
            return
        if ls < 0 or ls > index * 3:
            return False
        for i in range(1, 4):
            # This line, if s[:i] is None, there is no int(s[:i])
            if s[:i]:
                if i > 1 and s[0] == '0':
                    return False
                if int(s[:i]) < 256 and len(s[:i]) == i:
                    self.dfs(res, subset + s[:i] + '.', s[i:], index - 1)

if __name__ == '__main__':
    S = Solution()
    # test = S.restoreIpAddresses("25525511135")
    # test = S.restoreIpAddresses("0000")
    test = S.restoreIpAddresses("1111")
    print(test)
    # print(int('0'))