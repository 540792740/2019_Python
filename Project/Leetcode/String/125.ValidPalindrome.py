class Solution(object):
    # Two point
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1;
            r -= 1
        return True

    #isalnum
    def isPalindrome1(self, s):
        def clean(s):
            res = []
            for i in s:
                if i.isalnum():
                    res.append(i.lower())
            return res
        res = clean(s)
        print(res)
        print(res[::-1])
        if res[::-1] == res:
            return True
        else:
            return False
if __name__ == '__main__':
    S = Solution()
    a = S.isPalindrome1("A man, a plan, a canal: Panama")
    # a = S.isPalindrome(".,")
    # a = S.isPalindrome1("0p")
    print(a)