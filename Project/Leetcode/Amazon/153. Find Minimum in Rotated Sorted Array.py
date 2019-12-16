class Solution(object):
    def findMin(self, nums):
        if not nums: return 0
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]

    # Heapify min heap
    def findMin1(self, nums):
        heapq.heapify(nums)
        return nums[0]