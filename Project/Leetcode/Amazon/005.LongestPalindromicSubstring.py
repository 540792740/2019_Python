'''
0.  Make sure return when length is 0 and 1.
1.  write a loop of whole array with variable i,
    write another loop with variable j, from i + 1 to end.
    what i do to make same character together.
2.  find longest substring, shift left value and right value,
    if the value is equal, substring can be longer.
    record the length of substring.
3.  Find the longest substring and return it.
4.  Test function: length = 0, 1. try some unique array [abababbb], [abafxabba]

'''

class Solution(object):

    # 88%
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):

            # when odd number, 'aba'
            temp = self.helper(s, i, i)
            if len(temp) > len(res): res = temp
            # when even number, 'abba'
            temp = self.helper(s, i, i + 1)
            if len(temp) > len(res): res = temp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1: r]

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s
        if length == 2:
            if s[0] == s[1]:
                return s
            return s[0]
        max_length = 1
        res = s[0]
        i = 0
        while i < length:
            j = i + 1
            '''make same character aabbbbaa, bbbb together'''
            while j < length:
                if s[i] == s[j]:
                    j += 1
                else:
                    break

            k = 0
            print(i,j)
            '''left - 1, right + 1, find longest length'''
            while i - k - 1 >= 0 and j + k <= length - 1:
                if s[i - k - 1] !=s[j + k]:
                    break
                k += 1

            if j - i + 2 * k > max_length:
                print('s',j - i + 2*k)
                max_length = j - i + 2 * k
                res = s[i - k : j + k]
                # print(max_length,res)
            i = j
        return res

if __name__ == "__main__":
    S = Solution()
    # a = S.longestPalindrome("cbababd")
    a = S.longestPalindrome("aabbba")
    # a = S.longestPalindrome("bac")
    # a = S.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    print(a)
    a = {}
    a[1] = 'a'
    a['b'] = 1
    print(a)
