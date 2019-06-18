class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        count = 0
        ls = len(nums)
        if ls == 0:
            return ls
        while left < ls - count:
            if nums[left] == val:
                nums[left] = nums[ls - count - 1]
                count += 1
            else:
                left += 1
        return ls - count
