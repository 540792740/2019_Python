'''
Recursion
'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate(n,n,'',res)
        return res

    def generate(self, left, right, str, res):
           if left == 0 and right == 0:
               res.append(str)
           if left > 0:
               self.generate(left - 1, right, str+'(', res)
           if left < right:
               self.generate(left, right - 1, str+')', res)

if __name__ == '__main__':
    S = Solution()
    a = S.generateParenthesis(4)
    print(a)