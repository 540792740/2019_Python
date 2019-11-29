class Solution:
    def missingNumber(self, nums):
        ls = len(nums)
        return (ls * (ls + 1)) / 2 - sum(nums)

    def missingNumber1(self, nums):
        res = 0
        for i in range(len(nums)+ 1):
            res ^= i
            if i < len(nums):
                res ^= nums[i]
        return res