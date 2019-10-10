'''
0. use function .find

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        temp = s[0]
        max_len = 1
        for i in s[1:]:
            if i in temp:
                var = temp.find(i)
                temp = temp[var + 1:]
            temp += i
            if len(temp) > max_len:
                max_len = len(temp)
        return max_len

if __name__ == '__main__':
    S = Solution()
    a = S.lengthOfLongestSubstring("abcabcbb")
    a = "abcabcbb"
    print(a.find('c'))