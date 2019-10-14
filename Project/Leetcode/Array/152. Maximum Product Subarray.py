class Solution(object):
    def maxProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        Largest_p = [0] * length
        Smallest_p = [0] * length
        Largest_p[0] = Smallest_p[0] = res = nums[0]
        for i in range(1, length):
            Largest_p[i] = max(Largest_p[i - 1] * nums[i], nums[i], Smallest_p[i - 1] * nums[i])
            Smallest_p[i] = min(Largest_p[i - 1] * nums[i], nums[i], Smallest_p[i - 1] * nums[i])
            res = max(Largest_p[i], res)
        return res

    def maxProduct(self, nums):
        length = len(nums)
        Largest_p = Smallest_p = res = nums[0]
        for i in range(1, length):
            pre_largest, pre_Smallest = Largest_p, Smallest_p
            Largest_p =  max(pre_largest * nums[i], nums[i], pre_Smallest * nums[i])
            Smallest_p =  min(pre_largest * nums[i], nums[i], pre_Smallest * nums[i])
            res = max(res, Largest_p)
        return res
if __name__ == '__main__':
    S = Solution()
    a = S.maxProduct([2,-3,-2,-4])
    print(a)
    a = 1
    b= 1
    a,b = b,(b + 1)
    print(a,b)