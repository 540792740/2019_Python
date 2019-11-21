class Solution:
    def canJump(self, nums) :
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
            if m == len(nums): return True
        return True

    # 89% by myself
    def canJump(self, nums) :
        left_steps = len(nums) - 1
        could_jump = nums[0]
        if left_steps == 0: return True
        if could_jump == 0: return False
        for i in range(1, len(nums)):
            if could_jump > left_steps: return True
            could_jump -= 1
            could_jump = max(could_jump, nums[i])
            left_steps -= 1
            if could_jump == 0 and left_steps > 0: return False
        return True