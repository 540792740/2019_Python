'''
1. Fibonacci sequence
2. DP

'''

class Solution(object):
    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre = cur = 1
        for i in range(1, n):
            pre, cur = cur, pre + cur
        return cur

    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        steps = [1, 1]
        for i in range(2, n + 1):
            steps.append(steps[i - 1] + steps[i - 2])
        return steps[n]

if __name__ == '__main__':
    S = Solution()
    a = S.climbStairs1(5)
    b = S.climbStairs2(5)
    print(a,b)