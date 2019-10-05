'''
for this question
0.  make sure return when nums length 0, 1
1.  at first, maximum value is nums[0]
2.  write loop from nums[1] to end, next value should or not add to previous
    array. Compare the value with add new number to subarray or new subarray.

'''


class Solution(object):
    def maxSubArray(self, nums):
        ls = len(nums)
        if ls < 1:
            return 0
        else:
            num_next = nums[0]
            max_num = nums[0]
            for i in range(1, ls):
                num_next = max(nums[i], num_next + nums[i])
                max_num = max(max_num, num_next)
        return max_num


if __name__ == '__main__':
    S = Solution()
    a = S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    a = S.maxSubArray([1,2,3,4,-1,-2,-3,7])
    print(a)