'''
0. s is string, there is no s[i], s[j] = s[j], s[i], only list can do
1.
'''

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vows = set('aeiouAEIOU')
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and s[l] not in vows: l += 1
            while l < r and s[r] not in vows: r -= 1
            if l > r:
                break
            s[l],s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)





if __name__ == '__main__':
    S = Solution()
    a = S.reverseVowels("leetcode")
    print(a)