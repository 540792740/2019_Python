class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_rev = s[::-1]
        maxlen = 0
        dp = []
        length = len(s)
        if length <= 1:
            return s
        for i in range(length + 1):
            dp += [[0] * (length + 1)]
        for i in range(length):
            for j in range(length):
                if s[i] is s_rev[j]:
                    r = dp[i + 1][j + 1] = dp[i][j] + 1
                    if r >= maxlen:
                        maxlen = r
                        end = i
        print(end, maxlen)
        print(dp)
        return s[end - maxlen + 1 : end + 1]


if __name__ == "__main__":
    S = Solution()
    # a = S.longestPalindrome("bababd")
    a = S.longestPalindrome("aacdecaa")
    # a = S.longestPalindrome("bac")
    # a = S.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(a)

'''
class Solution(object):
def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    s_rev = s[::-1]
    max, loc = (0, 0)
    length = len(s)
    D0 = []
    for row in xrange(length+1): D0 += [[0]*(length+1)]
    for i in range(length):
        for j in range(length):
            if s[i] is s_rev[j]:
                Tmp = D0[i+1][j+1] = D0[i][j] + 1
                if max <= Tmp:
                    max, loc = Tmp, i
    return s[loc-max+1:loc+1]
'''