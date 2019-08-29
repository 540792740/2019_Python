'''
Easy
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ls = len(nums) - 1
        maj = int(ls / 2)
        return nums[maj]