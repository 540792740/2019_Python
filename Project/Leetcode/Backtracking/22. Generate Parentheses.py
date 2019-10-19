class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate(n, n, '', res)
        return res
    def generate(self, left, right, str, res):
        if left == 0 and right == 0:
            res.append(str)
        if left > 0:
            self.generate(left - 1, right, str + '(', res)
        if right > left:
            self.generate(left, right - 1, str + ')', res)