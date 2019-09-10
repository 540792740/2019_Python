class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = cur = 0
        for i in nums:
            pre, cur = cur, max(i + pre, cur)
        return cur


if __name__ == '__main__':
    S = Solution()
    a = S.rob([1,5,3,5,7,2,5,3,2,2])
    print(a)