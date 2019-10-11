'''
    if i <= len(s):
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ls = len(s)
        if ls < 4 or ls > 12:
            return None
        res = []
        self.dfs(res, s, 4, '')
        return res
    def dfs(self, res, s, index, subset):
        if index == 0:
            if not s:
                res.append(subset[:-1])
            return
        for i in range(1,4):
            if i <= len(s):
               if i == 1:
                    self.dfs(res, s[i:], index - 1, subset +s[:i]+'.')
               elif i == 2 and s[0] != '0':
                    self.dfs(res, s[i:], index - 1, subset +s[:i]+'.')
               elif i == 3 and s[0] != '0' and int(s[:3]) <=255:
                    self.dfs(res, s[i:], index - 1, subset +s[:i]+'.')

if __name__ == '__main__':
    S = Solution()
    a = S.restoreIpAddresses("25525511135")
    a = S.restoreIpAddresses("010010")
    print(a)