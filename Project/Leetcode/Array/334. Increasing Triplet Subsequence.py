class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ls = len(nums)
        if ls <= 2: return False
        ele_1 = nums[0]
        ele_2 = 2** 31 - 1
        for i in range(1, ls):
            if nums[i] <= ele_1: ele_1 = nums[i]
            elif nums[i] <= ele_2: ele_2 = nums[i]
            else: return True
        return False
