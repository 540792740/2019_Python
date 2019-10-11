class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split(' ')
        print(a)
        for i in range(len(a)):
            a[i] = a[i][::-1]
        return ' '.join(a)

if __name__ == '__main__':
    S = Solution()
    a = S.reverseWords("Let's take LeetCode contest")
    print(a)