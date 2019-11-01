class Solution(object):
    # 94%
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        l, r = 0, len(nums) - 1
        while  l < r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                for i in range(l, r + 1):
                    if nums[i] == target:
                        l = i
                        break
                for j in range(r, l - 1, -1):
                    if nums[j] == target:
                        r = j
                        break
                return [l, r]
        return [-1, -1]