class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[l]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    return nums[l]
            else:

                if r - l == 1:
                    return min(nums[l], nums[r])
                r = mid
        return nums[l]
    # 94%
    def findMin1(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid - 1] and nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] < nums[r]:
                right = mid
            else:
                left = mid + 1
        return nums[l]

