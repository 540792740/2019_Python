class Solution:
    # 86%
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        if r == -1: return
        # when length is bigger than 2
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1
        if nums[l] < nums[r]:
            return l
        else:
            return r

    # Regular Brute force
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = len(nums)
        if ls == 0: return None
        if ls == 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return ls - 1

        for i in range(1, ls - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

