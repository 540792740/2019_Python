class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s: return True
        l, r = 0, len(s) - 1
        while l <= r:
            if r - l in {0, 1}: return True
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return s[l : r] == s[l : r][::-1] or s[l + 1 : r + 1] == s[l + 1: r + 1][::-1]

if __name__ == '__main__':
    S = Solution()
    # test = S.validPalindrome("cbbcc")
    # print('Should be True', test)
    # test = S.validPalindrome("aba")
    # print('Should be True', test)
    test = S.validPalindrome("abc")
    print('Should be F', test)