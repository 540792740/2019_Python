class Solution:
    def canJump(self, nums) :
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
            if m == len(nums): return True
        return True

    # 86% by myself
    def canJump(self, nums) :
        ls = len(nums)
        left = 0
        jump = 1
        res_length = ls
        while left < ls - 1 and jump != 0:
            jump -= 1
            res_length -= 1
            jump = max(nums[left], jump)
            # print(jump, res_length)
            if jump >= res_length:
                return True
            left += 1
        if res_length > jump:
            return False
        else:
            return True