class Solution:
    def missingNumber(self, nums):
        ls = len(nums)
        return (ls * (ls + 1)) / 2 - sum(nums)


    # 10% slow
    def missingNumber1(self, nums):
        nums.sort()
        New_list = set(nums)
        for i in range(len(nums)):
            if i not in New_list:
                return i
        return i + 1