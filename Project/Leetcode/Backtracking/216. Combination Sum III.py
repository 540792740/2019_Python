'''
bymyself! 97%!!!!
'''


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        x = 0
        res = []
        def helper(n, subset, target):
            if target == 0 and len(subset) == k:
                res.append(subset)
                return
            if len(subset) == k:
                return
            for i in range(n, 0, -1):

                helper(i - 1, [i] + subset, target - i)
        helper(9, [], n)
        return res

if __name__ == '__main__':
    S = Solution()
    test = S.combinationSum3(3, 7)
    print(test)
    test = S.combinationSum3(2, 18)
    print(test)