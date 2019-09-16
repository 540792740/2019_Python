class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        if n == 0:
            return
        self.dp = [0] * n
        self.dp [0] = nums[0]
        for i in range(1,n):
            self.dp[i] = (nums[i] + self.dp[i - 1])
        print(self.dp)



    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.dp[j] - self.dp[i - 1]
        else:
            return self.dp[j]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)


if __name__ == '__main__':
    # S = NumArray([-2,0,3,-5,2,-1])
    S = NumArray([])
    a = S.sumRange()
    # a = S.sumRange(2,5)
    # a = S.sumRange(0,5)
    print(a)