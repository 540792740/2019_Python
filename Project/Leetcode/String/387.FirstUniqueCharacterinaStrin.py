'''
0. Save into a dic
1. Find value == 1 return index
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        index = - 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                index = i
                break
        return index