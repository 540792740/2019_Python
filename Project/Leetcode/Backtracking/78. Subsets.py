'''
Important: Backtracking, there should be nums[i + 1:] !! remember!
'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, res, [])
        return res
    def dfs(self, nums, res, subset):
        for i in range(len(nums)):
            self.dfs(nums[i + 1:], res, subset + [nums[i]])
        res.append(subset)
if __name__ == '__main__':
    S = Solution()
    test = S.subsets([1, 2, 3])
    print(test)
