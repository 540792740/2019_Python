'''
Microsoft LT
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        print(s)
        return ' '.join(reversed(s))


if __name__ == '__main__':
    S= Solution()
    a = S.reverseWords("the sky is blue")
    print(a)