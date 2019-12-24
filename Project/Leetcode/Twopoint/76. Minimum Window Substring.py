class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        res = ''
        l, count, minLen = 0, 0, 2 ** 31
        dic = {}
        for i in t: dic[i] = dic.get(i, 0) + 1
        for i, c in enumerate(s):
            dic[c] = dic.get(c, 0) - 1
            if dic[c] >= 0:
                count += 1
            while count == len(t):
                if minLen > i - l + 1:
                    minLen = i - l + 1
                    res = s[l : i + 1]
                dic[s[l]]  = dic.get(s[l], 0) + 1
                if dic[s[l]] > 0:
                    count -= 1
                l += 1
        return res

if __name__ == '__main__':
    S = Solution()
    test = S.minWindow("ADOBECODEBANC", "ABC")
    print(test)