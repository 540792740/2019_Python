class Solution(object):
    # 84%
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        ls = len(nums)
        if ls == 0: return 0
        i, j = 0, 0
        summary = 0
        res_length = ls + 1
        while summary < s and j < ls:
            summary += nums[j]
            j += 1
            while summary >= s:
                if j - i < res_length:
                    res_length = j - i
                summary -= nums[i]
                i += 1

        if res_length == ls + 1: return 0
        return res_length

