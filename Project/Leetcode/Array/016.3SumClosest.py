class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        ls = len(nums) - 1
        if len(nums) < 2:
            return []
        minium = abs(nums[i] + nums[i + 1] + nums[ls - 1] - target)
        while i < ls - 2:
            j = i + 1
            k = ls
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == target:
                    return target
                elif curr > target:
                    minium = min(minium, abs(curr - target))
                    k -= 1
                else:
                    j += 1
                    i += 1
        return minium

