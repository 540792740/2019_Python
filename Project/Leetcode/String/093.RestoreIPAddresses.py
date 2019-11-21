'''
    if i <= len(s):
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def dfs(subset, s, index):
            ls = len(s)
            if ls > index * 3 or ls < index: return
            if not s and subset[:-1] not in res:
                res.append(subset[:-1])
                return

            for i in range(1, 4):
                if s[:i]:
                    if i > 1 and s[0] == '0': return
                    if int(s[:i]) >= 0 and int(s[:i]) < 256:
                        dfs(subset + s[:i] + '.', s[i:], index - 1)

        dfs('', s, 4)
        return res
if __name__ == '__main__':
    S = Solution()
    a = S.restoreIpAddresses("25525511135")
    a = S.restoreIpAddresses("010010")
    print(a)