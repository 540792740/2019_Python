class Solution:
    # 97%
    def searchInsert(self, nums, target):

        # if not nums: return 0
        # if target <= nums[0]: return 0
        # if target > nums[-1]: return len(nums)
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        return l

    # 97% myself
    def searchInsert(self, nums, target):
        ls = len(nums)
        if target < nums[0]: return 0
        if target > nums[-1]: return ls
        for i in range(ls):
            if nums[i] == target:
                return i
            if i > 0 and i < ls :
                if target > nums[i -1] and target < nums[i]:
                    return i