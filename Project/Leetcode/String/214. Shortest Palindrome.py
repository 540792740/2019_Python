class Solution:
    def shortestPalindrome(self, s):
        print(s)
        if not s or len(s) == 1: return s
        j = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == s[j]: j += 1
        # print(s[::-1][:len(s) - j] )
        return s[::-1][:len(s) - j] + self.shortestPalindrome(s[:j - len(s)]) + s[j - len(s):]

if __name__ == '__main__':
    S = Solution()
    # test = S.shortestPalindrome('abcd')
    # print(test)
    test = S.shortestPalindrome('aacecaaa')
    print(test)