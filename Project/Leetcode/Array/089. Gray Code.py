'''
No meaning
'''

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        res = [0, 1]
        for i in range(2, n + 1):
            for j in range(len(res) - 1, -1 , -1):
                res.append(res[j] | 1 << i - 1)
        return res

if __name__ == '__main__':
    S = Solution()
    test = S.grayCode(3)
    print(test)
    print(3 | 2 << 1)