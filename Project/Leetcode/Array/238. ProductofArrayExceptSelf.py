'''
0. when there is no '0'
1. when there is only 1 '0'
2. when there are more than 1 '0'

'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pro = 1
        count_0 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 += 1
                if count_0 == 1:
                    continue
                elif count_0 > 1:
                    for i in range(len(nums)):
                        nums[i] = 0
                    return nums
            pro *= nums[i]
        for i in range(len(nums)):
            if count_0 == 0:
                nums[i] = pro // nums[i]
            if count_0 == 1:
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = pro
        return nums

if __name__ == '__main__':
    S = Solution()
    a = S.productExceptSelf([1,2,0])
    a = S.productExceptSelf([0,2,0])
    print(a)