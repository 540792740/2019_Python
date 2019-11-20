class Solution(object):
    # 98%
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                temp1, temp2 = mid, mid
                while temp1 - 1 >= l and nums[temp1 - 1] == target:
                    temp1 -= 1
                while temp2 + 1 <= r and nums[temp2 + 1] == target:
                    temp2 += 1
                return [temp1, temp2]
        return [-1, -1]
