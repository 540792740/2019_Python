class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        ls = len(nums)
        for i in range(0, ls, 2):
            sum += nums[i]
        return sum
if __name__ == '__main__':
    S = Solution()
    a = S.arrayPairSum([1,2,3,4,5,6])
    print(a)