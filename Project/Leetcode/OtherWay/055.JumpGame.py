class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ls = len(nums)
        i = 0
        next_num = 0
        while i < ls:
            next_num = max(i + nums[i], next_num)
            if ls - 1 <= next_num:
                return True
            if i < next_num:
                i += 1
            else:
                return False

if __name__ == '__main__':
    S = Solution()
    a = S.canJump([2,3,1,1,0,4])
    a = S.canJump([0])
    print(a)