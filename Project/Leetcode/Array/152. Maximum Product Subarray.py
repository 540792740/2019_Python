'''
dp
'''

class Solution(object):
    def maxProduct(self, nums):
        ls = len(nums)
        Largest_p = Smallest_p = res = nums[0]
        for i in range(1, ls):
            pre_largest, pre_Smallest = Largest_p, Smallest_p
            Largest_p =  max(pre_largest * nums[i], nums[i], pre_Smallest * nums[i])
            Smallest_p =  min(pre_largest * nums[i], nums[i], pre_Smallest * nums[i])
            res = max(res, Largest_p)
        return res
if __name__ == '__main__':
    S = Solution()
    a = S.maxProduct([2,-3,-2,-4])
    print(a)