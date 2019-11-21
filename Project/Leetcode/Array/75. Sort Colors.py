class Solution:

    # 97.53
    def sortColors(self, nums):
        l, r = 0, len(nums) -1
        red_index = 0
        while l <= r:
            if nums[l] == 1:
                l += 1
            elif nums[l] == 2:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
            else:
                nums[l], nums[red_index] = nums[red_index], nums[l]
                red_index += 1
                l += 1
        return nums