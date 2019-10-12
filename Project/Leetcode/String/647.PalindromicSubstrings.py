class Solution(object):

    # Two point 80 %
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            count += 1
            # uneven number / odd number
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            # Even number
            left = i
            right = i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
        return count

    # O(n**3)   14%
    def countSubstrings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        ls = len(s)
        for i in range(ls):
            for j in range(ls,i, -1):
                if s[i:j] == s[i:j][::-1]:
                    res += 1
        return res

    # DP 30%
    # def countSubstrings2(self, s):
    #     n = len(s)
    #     count = 0
    #     start, end, maxL = 0, 0, 0
    #     dp = [[False] * n for i in range(n)]
    #     for i in range(n):
    #         for j in range(i):
    #             dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
    #             if dp[j][i]:
    #                 count += 1
    #         dp[i][i] = 1
    #         count += 1
    #     return count
if __name__ == '__main__':
    S = Solution()
    a = S.countSubstrings("aaa")
    a = S.countSubstrings2("aaaBBCC")
    print(a)
